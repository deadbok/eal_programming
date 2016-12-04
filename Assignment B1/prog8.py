#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 8
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (6/11-2016)

Calculate the total price of a meal purchased at a restaurant.
'''


def main():
    '''
    Program main entry point.
    '''
    # Get the amount of purchase from the user.
    try:
        total_purchase = float(input('Enter the price of the meal: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Calculate the tip.
    tip = total_purchase * 0.15
    # Calculate the sales tax
    tax = total_purchase * 0.07

    # Print the totals
    # Use new style Python 3 format strings.
    # {:12.2f} means align for a total of 12 digits with 2 digits
    # after the decimal point.
    print('\nTotal purchase:\t\t{:12.2f}'.format(total_purchase))
    print('Tip (15%):\t\t\t{:12.2f}'.format(tip))
    print('Sales tax (7%):\t\t{:12.2f}'.format(tax))
    print('Final total:\t\t{:12.2f}'.format(total_purchase + tip + tax))


# Run this when invoked directly
if __name__ == '__main__':
    main()
