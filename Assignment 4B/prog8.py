#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 8
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-10)

Calculate the sum of numbers input by the user.
'''


def main():
    '''
    Program main entry point.
    '''
    # List to keep the numbers enteret by the user.
    numbers = list()
    # Get numbers from the user.
    try:
        print('\nInput a series of numbers, end inputting by entering a ' +
              'negative number')
        number = float(input('Input a number: '))
        while number > -1:
            numbers.append(number)
            number = float(input('Input a number: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print('The sum af all numbers entered is: {:0.2f}'.format(sum(numbers)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
