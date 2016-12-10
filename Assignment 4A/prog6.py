#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 6
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Output a table with the range 0-20 degrees celsius converted to degrees
Fahrenheit.
"""


def cel2fah(celsius = 0):
    '''
    Convert degrees celsius to Fahrenheit

    :param celsius: Degrees celsius.
    :return: Degrees Fahrenheit.
    '''
    return (9 / 5) * celsius + 32


def main():
    '''
    Program main entry point.
    '''
    # Print a header.
    print('Conversion table from degrees Celsius to degrees Fahrenheit:\n')
    print('Celsius\t\tFahrenheit')
    print('-----------------------')
    # Print a table of Celsius conversions from 0-20
    for celsius in range(0, 21):
        print('{:6}\t\t'.format(celsius) +
              '{:9.2f}'.format(cel2fah(celsius)))

# Run this when invoked directly
if __name__ == '__main__':
    main()
