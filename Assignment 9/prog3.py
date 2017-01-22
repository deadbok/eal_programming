#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1 "Date Printer"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-22)

A program that reads a date in the form mm/dd/yyyy from the user and reformat
it to the form March 12, 2012.
'''
from datetime import datetime

def get_date():
    """
    Get a date of the form mm/dd/yyyy, complain if input is wrong.

    :return: A datetime object.
    """
    date_str = input('Input a date in the form mm/dd/yyyy: ')

    # Do sanity check of the input.
    try:
        # Use the datetime object function strptime to from correct form,
        # gives us free validation of the input.
        date = datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease enter a date of the form mm/dd/yyyy.')
        exit(1)

    return date

def main():
    '''
    Main entry point.
    '''
    date = get_date()
    # Use the datetime object function strftime to convert to the correct form.
    print('\nThe date is: {}'.format(date.strftime('%B %d, %Y')))


# Run this when invoked directly
if __name__ == '__main__':
    main()
