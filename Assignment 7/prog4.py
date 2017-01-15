#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4 "World Series Champions"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-15)

Get 20 numbers from the user put them in a list and show:

 * The lowest number in the list
 * The highest number in the list
 * The total of the numbers in the list
 * The average of the numbers in the list.
"""


def get_numbers(numbers):
    """
    Get some numbers from the user.

    :param numbers: Number of numbers to generate.
    :return: A list of random numbers.
    """
    # Create the list.
    number_list = list()
    # Ask nicely.
    print('Please input {} numbers:'.format(numbers))
    try:
        # Counter for the output.
        i = 0
        # Ask for each number.
        for number in range(numbers):
            i += 1
            number_list.append(float(input('\tInput {}. number: '.format(i))))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    return (number_list)


def print_numbers_info(numbers):
    """
    Print info about a list of numbers

    :param numbers: The list of numbers.
    """
    # The numbers, sorted.
    sorted_numbers = sorted(numbers)

    # Print them
    print('The sorted numbers are:\n\t{}'.format(
        '\n\t'.join(['{:13.2f}'.format(number) for number in sorted_numbers])))
    print()
    # Print the rest of the info.
    print('The lowest number is: {:.2f}'.format(sorted_numbers[0]))
    print('The highest number is: {:.2f}'.format(sorted_numbers[-1]))
    print('The total of the numbers is: {:.2f}'.format(sum(numbers)))
    print('The average of the numbers is: {:.2f}'.format(
        sum(numbers) / len(numbers)))


def main():
    """
    Program main entry point.
    """
    # Handle the input in a list.
    numbers = list()
    numbers = get_numbers(20)

    print()

    print_numbers_info(numbers)


# Run this when invoked directly
if __name__ == '__main__':
    main()
