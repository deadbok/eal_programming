#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1 "Feet to Inches"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-10)

Convert feet to inches.
'''


def feet_to_inches(feet):
    """
    Convert feet to inches.

    :param feet: Number of feet.
    :return: Number of inches.
    """
    # Return the result of the conversion
    return(feet * 12)

def get_feet():
    """
    Get the number of feet from the user.

    :return: Number of feet.
    """
    try:
        return (float(input('Input number of feet: ')))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

def main():
    '''
    Main entry point.
    '''
    # Get number of feet.
    feet = get_feet()
    # Do calculation.
    inches = feet_to_inches(feet)
    # Output result.
    print('{:.2f} feet amounts to {:.2f} inches.'.format(feet, inches))

# Run this when invoked directly
if __name__ == '__main__':
    main()
