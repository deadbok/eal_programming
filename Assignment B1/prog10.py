#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 10
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (6/11-2016)

Stock Transaction Program.
'''


def main():
    '''
    Program main entry point.
    '''
    # This is the constants for the transaction.
    shares = 1000.0
    commission = 0.02
    bought_price_per_share = 32.87
    sold_price_per_share = 33.92

    # Calculate commissions.
    bought_commission = bought_price_per_share * shares * commission
    sold_commission = sold_price_per_share * shares * commission
    # Get the amount paid for the purchase/sale.
    total_price_bought = bought_commission + bought_price_per_share * shares
    total_price_sold = sold_price_per_share * shares - sold_commission

    ###########################################################################
    # Output:
    # * The amount of money Joe paid for the stock.
    # * The amount of commission Joe paid his broker when he bought the stock.
    # * The amount that Joe sold the stock for.
    # * The amount of commission Joe paid his broker when he sold the stock.
    # * Display the amount of money that Joe had left when he sold the stock
    #   and paid his broker (both times). If this amount is positive, then Joe
    #   made a profit. If the amount is negative, then Joe lost money.
    #
    # Use new style Python 3 format strings.
    # {:12.2f} means align for a total of 12 digits with 2 digits after the
    # decimal point.
    print('\nTotal stock price when bought:\t\t',
          '{:12.2f}'.format(total_price_bought))
    print('Commission paid when bought:\t\t',
          '{:12.2f}'.format(bought_commission))
    print('Total stock price when sold:\t\t',
          '{:12.2f}'.format(total_price_sold))
    print('Commission paid when sold:\t\t\t',
          '{:12.2f}'.format(sold_commission))
    print('Total win/loss of the transaction:\t',
          '{:12.2f}'.format(total_price_sold - total_price_bought))


# Run this when invoked directly
if __name__ == '__main__':
    main()
