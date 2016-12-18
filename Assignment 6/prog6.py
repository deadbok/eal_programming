#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: prog6.py
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-18)

A program that calculates the avarage of a list of comma seperated integers.
"""


def main():
    '''
    Program main entry point.
    '''
    try:
        # Open 'numbers.txt' for reading.
        with open('numbers.txt', 'r') as numbers_file:
            # Get the number form the file.
            numbers = numbers_file.readline()
            # Show them.
            print('Numbers in numbers.txt: ' + numbers)
            # Convert them to a list of integers using list comprehensions.
            numbers = [int(x) for x in numbers.split(',')]
            # Print the total sum.
            print('The average of the numbers: {:.2f}'.format(sum(numbers) / len(numbers)))
    except IOError as ex:
        # Complain when something goes wrong with the file access.
        print('Exception: {}'.format(str(ex)))
        print('Error reading "numbers.txt".')
        exit(1)
    except ValueError:
        print('File should contain only comma separated numbers.')
        exit(1)


# Run this when invoked directly
if __name__ == '__main__':
    main()
