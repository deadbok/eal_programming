#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: countcode.py
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-05-03)

Count the lines of Python code in files in the paths given on the commend line.
"""
import argparse
import os
import fnmatch
import filecmp

__VERSION__ = '1.0.0'


def parse_commandline():
    """
    Parse command line arguments.
    
    :return: A tuple with a list of files path to include, and a list of paths
             to exclude.
    """
    # Set up the arguments to have included paths as positional arguments,
    # and excluded path using --exclude.
    parser = argparse.ArgumentParser(description='Count lines of Python ' +
                                                 'code in given paths.')
    # Include parameter, at least one entry is needed.
    parser.add_argument('include', default=['.'], nargs='+',
                        help='Path to include')
    # Eclude paramater.
    parser.add_argument('--exclude', dest='exclude', nargs='*',
                        help='Path to exclude')

    # Parse command line
    args = parser.parse_args()

    # Print resulting paths
    print('Include paths:')
    for path in args.include:
        print('\t{}'.format(path))
    if args.exclude is not None:
        print('Exclude paths:')
        for path in args.exclude:
            print('\t{}'.format(path))

    # Return the paths.
    return ((args.include, args.exclude))


def scan_in_path(include_paths, exclude_paths):
    """
    Scan a path for Python files.
    
    :param include_paths: List of path to include when scanning.
    :param exclude_paths: List of paths to exclude when scanning. 
    :return: A tuple with the number of total files, duplicate files,
             excluded files, blank lines, comment lines, python lines,
             total lines.
    """
    # These are used to keep track of the totals
    blank_lines = 0
    comment_lines = 0
    python_lines = 0
    total_lines = 0
    total_files = 0
    duplicate_files = 0
    excluded_files = 0

    # Keep track of scanned files.
    files = {}

    # Run through all include paths
    for include_path in include_paths:
        # Use os.walk to recursivly decent the directories
        for root, dirnames, filenames in os.walk(include_path):
            # Find all .py files in th path.
            for filename in fnmatch.filter(filenames, '*.py'):
                #String containing the status of current file.
                status='c'
                # String containing text to append to teh status message for extra info.
                extra = ''

                #Assemble the current path.
                current_path = os.path.join(root, filename)

                # Check if current path matches an excluded path
                exclude = False
                for ex in exclude_paths:
                    if root.startswith(ex):
                        exclude = True
                        excluded_files += 1
                        extra += 'path: {} '.format(ex)
                        # Put a '-' in front of the path if excluded.
                        status = '-'

                # Check for duplicates if not ecluded.
                if not exclude:
                    if (filename in files.keys()):
                        # If the file name has been seen before.
                        for last_path in files[filename]:
                            # Exclude might have been updated.
                            if not exclude:
                                # Compare old and new file.
                                if filecmp.cmp(last_path, current_path):
                                    # If equal, exclude the new one.
                                    exclude = True
                                    duplicate_files += 1
                                    extra += 'duplicate: {} '.format(last_path)
                                    # Put a 'd' in front of the path if it is a
                                    # duplicate.
                                    status = 'd'
                    else:
                        # Create a new entry if the file has not been seen
                        # before.
                        files[filename] = []

                # If not count lines in the file.
                if not exclude:
                    # Count the lines.
                    lines = count_lines(current_path)

                    # Update counts.
                    blank_lines += lines[0]
                    comment_lines += lines[1]
                    python_lines += lines[2]
                    total_lines += lines[3]
                    total_files += 1

                    # Add the current path to known files.
                    files[filename].append(current_path)

                if status == 'c':
                    # Print terse count.
                    count = 'b:{0},c:{1},p:{2},t:{3}'.format(blank_lines,
                                                           comment_lines,
                                                           python_lines,
                                                           total_lines)
                else:
                    count = ''


                # Print the current path.
                print('{0}\t{1}, {2}, {3}'.format(status, current_path, count, extra))

    # Return the counts.
    return (
        total_files, duplicate_files, excluded_files, blank_lines,
        comment_lines,
        python_lines, total_lines)


def count_lines(path):
    """
    Scan a path for Python files.

    :param path: Path to file to process.
    :return: A tuple with the blank lines, comment lines, python lines,
             total lines.
    """
    # Open the file.
    with open(path, 'r', encoding="latin-1") as python_file:

        # Reset counters.
        blank_lines = 0
        comment_lines = 0
        python_lines = 0
        total_lines = 0

        # Run through all lines in the file.
        for line in python_file.readlines():
            # Add to total lines.
            total_lines += 1

            # Remove trailing spaces and tabs.
            line = line.lstrip(' \t')

            # Check for a blank line.
            if line.startswith('\n'):
                blank_lines += 1
            # Check for a comment.
            elif line.startswith('#'):
                comment_lines += 1
            # Count as a line of Python code.
            else:
                python_lines += 1

    # Return count.
    return (blank_lines, comment_lines, python_lines, total_lines)


def main():
    """
    Program main entry point.
    """
    # Print welcome message
    print('codecount.py v{} by Martin B. K. Grønholdt\n'.format(__VERSION__))
    # Parse the command line.
    paths = parse_commandline()

    # Scan all files.
    print('\nScanning selected Python files...')
    total_files, duplicate_files, excluded_files, blank_lines, comment_lines, python_lines, total_lines = scan_in_path(
        paths[0], paths[1])

    # Print result.
    print('\nTotals:')
    print('\tFiles: {}'.format(total_files))
    print('\tDuplicate files: {}'.format(duplicate_files))
    print('\tExcluded files: {}'.format(excluded_files))
    print('\tLines: {}'.format(total_lines))
    print('\tBlank lines: {}'.format(blank_lines))
    print('\tComment lines: {}'.format(comment_lines))
    print('\tPython code lines: {}'.format(python_lines))


# Run this when invoked directly
if __name__ == '__main__':
    main()
