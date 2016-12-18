#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: prog7.py
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-18)

A program that writes random integers to a file.
"""
from random import randrange
import os


def main():
    '''
    Program main entry point.
    '''
    # Get a file name and the number of integers to write to it.
    try:
        filename = input('Enter a file name to write the random integers to: ')
        count = int(input('Enter number of random integers to generate: '))
        # Complain when something unexpected was entered.
    except ValueError:
        print('Please use only numbers.')
        exit(1)
    except Exception as ex:
        print('Exception: {}'.format(str(ex)))
        print('\nSomething went wrong, try another name.')
        exit(1)

    # Check and warn if the file exists.
    if os.path.exists(filename):
        print('WARNING: Path exists are you sure you want to continue ' +
              'overwriting (y to continue)? ', end='')
        if input() != 'y':
            exit(0)

    try:
        # Open the file.
        with open(filename, 'w') as number_file:
            # Write the correct number of entries.
            for i in range(0, count):
                number = randrange(0, 100)
                if i > 0:
                    # Generate a Comma Separated File.
                    number_file.write(',')

                number_file.write(str(number))
                print('{}, '.format(number), end='')
        print('done.')
    except IOError:
        print('Error writing file.')
        exit(1)


# Run this when invoked directly
if __name__ == '__main__':
    main()
