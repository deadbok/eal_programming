#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (19/11-2016)

Convert to roman numerals.
'''


def to_roman(number=1):
    '''
    Convert a number in to a string with Roman numerals.

    :param number: Number to convert (between, and including, 1 and 10)
    :return: A string with the with the Roman numeral representation.
    '''
    # Look up table for each number.
    roman_look_up = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                     6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
    # Return the Roman numeral using the look up.
    return (roman_look_up[number])


def main():
    '''
    Main entry point.
    '''
    # Get the amount of kilometres from the user.
    try:
        number = int(input('Input a number in the range of 1 through 10: '))
        if (number < 1) or (number > 10):
            raise ValueError
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers in the range of 1 through 10.')
        exit(1)

    print('\n{} is "{}" in Roman numerals.'.format(number, to_roman(number)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
