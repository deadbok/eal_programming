#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1 "Total Sales"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-15)

Compute the total sale for a week.
'''


def get_sales(weekdays):
    """
    Get the sales figure for each day from the user.

    :param weekdays: Weekdays to get the sales figures for.
    :return: A list of the sales figures for the week.
    """
    # Create the sales list, holding sale figures.
    sales = list()

    try:
        # Ask for the sales figure for each day.
        for day in weekdays:
            sales.append(float(input('Input sales for {:10}: '.format(day))))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    return (sales)


def print_sales(weekdays, sales):
    """
    Print the sales and the acumulated total.

    :param weekdays: Weekdays to print the sales for.
    :return: Nothing.
    """
    # Index into the lists
    i = 0
    # Sum of sales
    sum = 0
    # Print the header
    print(' {:10}|{:^9} | {:9}'.format('Week day', 'Sale', 'Total'))
    print('-' * 33)
    # Print row for each day
    for i in range(len(weekdays)):
        sum += sales[i]
        print(' {:10}|{:9.2f} |{:9.2f}'.format(weekdays[i], sales[i], sum))


def main():
    '''
    Main entry point.
    '''
    # List of the days for that are calculated.
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']
    # Get number of feet.
    sales = get_sales(weekdays)
    print()
    # Output result.
    print_sales(weekdays, sales)


# Run this when invoked directly
if __name__ == '__main__':
    main()
