#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Calculate the county and state sales tax, and the final total of a purchase.
'''
def county_tax(total_purchase = 0):
    '''
    Calculate the county tax of 2% of the total purchase.

    :param total_purchase: Amount spend on the purchase in total.
    :return: Amount of county tax.
    '''
    # Calculate the county tax.
    return(total_purchase * 0.02)


def state_tax(total_purchase=0):
    '''
    Calculate the state tax of 4% of the total purchase.

    :param total_purchase: Amount spend on the purchase in total.
    :return: Amount of state tax.
    '''
    # Calculate the state tax
    return(total_purchase * 0.04)


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

    # Print the totals
    # Use new style Python 3 format strings.
    # {:12.2f} means align for a total of 12 digits with 2 digits
    # after the decimal point.
    print('\nTotal purchase:\t\t\t{:12.2f}'.format(total_purchase))
    print('State sales tax (4%):\t{:12.2f}'.format(state_tax(total_purchase)))
    print('County sales tax (2%):\t{:12.2f}'.format(county_tax(total_purchase)))
    print('Final total:\t\t\t{:12.2f}'.format(total_purchase +
                                              state_tax(total_purchase) +
                                              county_tax(total_purchase)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
