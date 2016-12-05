#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 3
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Calculate budget by first entering income and than expenses until '0' is
entered.
'''
def main():
    '''
    Program main entry point.
    '''
    try:
        budget = float(input('Input the amount of money budgeted for' +
                             'a month: '))

        print('\nInput expenses, end inputting by entering "0"')
        expense = float(input('Input expense: '))
        while expense > 0:
            budget -= expense
            print("\nCurrent amount of budget left: {:0.2f}\n".format(budget))
            expense = float(input('Input expense: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print("\nFinal amount of budget left: {:0.2f}\n".format(budget))
# Run this when invoked directly
if __name__ == '__main__':
    main()
