#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 7
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (6/11-2016)

Calculate miles-per-gallon for a given set of miles and gallons.
'''


def main():
    '''
    Program main entry point.
    '''
    # Get the data from the user.
    try:
        miles = float(input('Enter the distance in miles: '))
        gallons = float(input('Enter the gas used in gallons: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Miles per gallon.
    mpg = miles / gallons

    # Print mpg
    # Use new style Python 3 format strings.
    # {:0.2f} means 2 digits after the decimal point.
    print('\n{:0.2f} miles using'.format(miles),
          '{:0.2f} gallons of gas is'.format(gallons),
          '{:0.2f} miles per gallon.'.format(mpg))


# Run this when invoked directly
if __name__ == '__main__':
    main()
