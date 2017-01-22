#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2 "Sum of Digits in a String"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-22)

A program that ask for a string non separated of numbers, and sums of each
digit of the input.
'''
def get_numbers():
    """
    Get a string of numbers from the user.

    :return: A list all numbers.
    """
    # List for the numbers.

    numbers = list()

    number_str = input('Input a string of non-separated digits: ')

    try:
        #Convert each character to an int, fail and complain if something
        #cannot be converted.
        for ch in number_str:
            numbers.append(int(ch))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\n"{}" is not a number. Please use only numbers.'.format(ch))
        exit(1)

    return numbers

def main():
    '''
    Program main entry point.
    '''

    numbers = get_numbers()
    print("\nThe numbers are: {}".format(str(numbers).strip('[]')))
    print("The sum is: {:0.2f}".format(sum(numbers)))

# Run this when invoked directly
if __name__ == '__main__':
    main()
