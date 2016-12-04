#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 9
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (6/11-2016)

Convert Celsius temperatures to Fahrenheit temperatures.
'''


def main():
    '''
    Program main entry point.
    '''
    # Get the amount of purchase from the user.
    try:
        celcius = float(input('Enter temperature in degrees Celsius: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Calculate the county tax.
    fahrenheit = (9 / 5) * celcius + 32

    # Print the totals
    # Use new style Python 3 format strings.
    # {:0.2f} means 2 digits after the decimal point.
    print('\n{:0.2f} degrees Celcius is'.format(celcius),
          '{:0.2f} degrees Fahrenheit.'.format(fahrenheit))


# Run this when invoked directly
if __name__ == '__main__':
    main()
