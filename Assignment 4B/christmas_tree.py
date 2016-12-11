#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Christmas Tree
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-11)

Print a christmas tree.
"""
from random import randrange

from colorama import Fore


def stem(tree_width, stem_width):
    '''
    Print the stem of the christmas tree.

    :param tree_width: Width of the christmas tree.
    :param stem_width: Width of the christmas tree stem.
    :return: Nothing.
    '''
    # Find the offset where the stem starts
    stem_start = int(tree_width / 2 - 1)
    for h in range(0, 2):
        # Loop until the end of the stem.
        for w in range(0, stem_start + stem_width):
            if w < stem_start:
                # Non stem position, print space.
                print(' ', end='')
            else:
                # Stem position, print #.
                print(Fore.RED + '#', end='')
        print()


def print_tree_char(dist):
    '''
    Print one character of the actual tree. Chooses randomly among the rest of
    the characters available.

    :param dist:
    :return:
    '''
    count = sum([c[1] for c in dist])

    # We're at the last character.
    if count == 1:
        i = 0
        # Don't waste time, just find it.
        while dist[i][1] == 0:
            i += 1

        # And print it.
        dist[i] = (dist[i][0], dist[i][1] - 1)
        print(dist[i][0])
    # Some other character in the tree.
    else:
        # Pick a random character among the rest needed.
        choice = randrange(0, count)

        # Find the choice by distributing them among all the possible characters
        # in the tree.
        i = 0
        while choice > sum([c[1] for c in dist[0:i + 1]]):
            i += 1

        # Bad choice, all used up.
        if dist[i][1] == 0:
            # Make another choice
            return (print_tree_char(dist))
        else:
            # Print the character.
            dist[i] = (dist[i][0], dist[i][1] - 1)
            print(dist[i][0], end='')

    return (dist[i][0])


def tree(width, height, stem_width, dist):
    '''
    Print the tree.

    :param height: Height, in characters, of the tree.
    :param stem_width: Width, in characters, of the tree.
    :param dist: Characters and the number to be used in the tree.
    :return:
    '''
    # Get the area.
    n_chars = 0
    for i in range(0, 12):
        n_chars += i * 2 + 1

    # Dictionary of chars, and how many have been used.
    use = dict()
    # Create a dictionary to keep a record of the number of used characters.
    for char in dist:
        # Add all characters to the dictionary with 0 used.
        use[char[0]] = 0

    # Find the middle of the tree.
    tree_middle = int(width / 2)
    # Row width of the top.
    row_width = 1
    # Loop from the top down.
    for h in range(0, height):
        # New line.
        print()
        # Loop from left to right.
        for w in range(0, tree_middle + row_width):
            # Print the filling spaces before the tree.
            if w < (tree_middle - int(row_width / 2)):
                print(' ', end='')
            # Print the top.
            elif row_width == 1:
                # A star at the top.
                i = 0
                while '*' not in dist[i][0]:
                    i += 1

                # Print the character.
                dist[i] = (dist[i][0], dist[i][1] - 1)
                print(dist[i][0], end='')
                # Add to used
                use[dist[i][0]] += 1
            # Print the rows of the tree itself.
            elif w <= (tree_middle + int(row_width / 2)):
                use[print_tree_char(dist)] += 1

        # Next row is wider.
        row_width += 2

    stem(width, stem_width)
    return(use)


def main():
    '''
    Program main entry point.
    '''
    # Height of the tree, and stem width.
    height = 1
    stem_width = 3

    try:
        height = int(input('Input the height of the christmas tree: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Get the number of characters in the tree.
    n_chars = 0
    for i in range(0, height):
        n_chars += i * 2 + 1
    width = i * 2 + 1

    # Set number of characters for each type of decorations.
    tree_chars = [
        (Fore.MAGENTA + 'O', int((n_chars / 100) * 10)),
        (Fore.LIGHTWHITE_EX + 'i', int((n_chars / 100) * 10)),
        (Fore.LIGHTRED_EX + 'V', int((n_chars / 100) * 10)),
        (Fore.LIGHTYELLOW_EX + '*', int((n_chars / 100) * 10)),
        (Fore.GREEN + '#', int((n_chars / 100) * 60))]

    # Fix rounding errors by adding more green.
    tree_chars[4] = (tree_chars[4][0], tree_chars[4][1] + n_chars -
                     sum([c[1] for c in tree_chars]))

    # Print the tree after a new line.
    print()
    use = tree(width, height, stem_width, tree_chars)

    # Print statistics after a new line.
    print()
    total_number = 0
    total_percent = 0
    print(Fore.WHITE + ' Type |   Nr.  |  Percent')
    print(Fore.WHITE + '-------------------------------')
    for char, number in use.items():
        percent = number / (n_chars / 100)
        print('  {}'.format(char) + Fore.WHITE +
              '   |{:6}  | {:6.2f}%'.format(number, percent))
        total_number += number
        total_percent += percent
    print(Fore.WHITE + '-------------------------------')
    print(Fore.WHITE + '      |{:6}  | {:6.2f}%'.format(total_number, total_percent))


# Run this when invoked directly
if __name__ == '__main__':
    main()
