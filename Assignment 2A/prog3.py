#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 3
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Calculate the minimum amount of insurance, given the replacement cost of a
building.
'''
def minimum_insurance(replacement_cost = 0):
    '''
    Calculate the county tax of 2% of the total purchase.

    :param replacement_cost: The replacement cost of the building.
    :return: Minimum insurance sum.
    '''
    # Calculate minimum insurance sum.
    return(replacement_cost * 0.80)


def main():
    '''
    Program main entry point.
    '''
    # Get the amount of purchase from the user.
    try:
        replacement_cost = float(input('Enter the replacement cost of the ' +
                                       'building: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Print the totals
    # Use new style Python 3 format strings.
    # {:12.2f} means align for a total of 12 digits with 2 digits
    # after the decimal point.
    print('\nBuilding replacemnent cost:\t\t' +
          '{:12.2f}'.format(replacement_cost))
    print('Minimum insurance sum (80%):\t' +
          '{:12.2f}'.format(minimum_insurance(replacement_cost)))



# Run this when invoked directly
if __name__ == '__main__':
    main()
