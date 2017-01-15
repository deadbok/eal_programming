#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2 "Lottery Number Generator"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-15)

A program that generates seven lottery numbers.
'''
import random


def get_lottery_numbers():
    """
    Get the result from the user.

    :return: User result.
    """
    # Create a list of 7 random numbers in the range 0-9
    return ([random.randrange(9) for _ in range(7)])


def print_lottery_numbers(numbers):
    """
    Print an addition puzzle.

    :return: The result of the addition.
    """
    # Print the list by turning all entries into strings and adding ', '
    print('\t{}'.format(', '.join([str(number) for number in numbers])))


def main():
    '''
    Program main entry point.
    '''
    # Welcome message.
    print('Generated lottery numbers:')
    # Generate the numbers
    numbers = get_lottery_numbers()
    print()
    # Print them
    print_lottery_numbers(numbers)


# Run this when invoked directly
if __name__ == '__main__':
    main()
