#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 6
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (6/11-2016)

Calculate the county and state sales tax, and the final total of a purchase.
'''


def main():
    '''
    Program main entry point.
    '''
    # Get the amount of purchase from the user.
    try:
        total_purchase = float(input('Enter the amount of a purchase: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Calculate the county tax.
    county_tax = total_purchase * 0.02
    # Calculate the state tax
    state_tax = total_purchase * 0.04

    # Print the totals
    # Use new style Python 3 format strings.
    # {:12.2f} means align for a total of 12 digits with 2 digits
    # after the decimal point.
    print('\nTotal purchase:\t\t\t{:12.2f}'.format(total_purchase))
    print('State sales tax (4%):\t{:12.2f}'.format(state_tax))
    print('County sales tax (2%):\t{:12.2f}'.format(county_tax))
    print('Final total:\t\t\t{:12.2f}'.format(
        total_purchase + state_tax + county_tax))


# Run this when invoked directly
if __name__ == '__main__':
    main()
