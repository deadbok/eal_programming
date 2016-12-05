#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 5
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Calculate the avarage rainfall over a period of years.
"""


def get_rain_year():
    '''
    Get the monthly rainfall for a year.

    :return: Array of rainfall each month
    '''
    # Create list for the values.
    months = list()
    # Loop through month.
    for month in range(1, 13):
        print('Input amount of rain for month number {} '.format(month) +
              '( in inches): ', end='')
        # Add the amount to the list
        months.append(float(input()))
    # Return the list
    return months


def main():
    '''
    Program main entry point.
    '''
    # Number of years.
    years = 0
    # List of list of values for all months of all years.
    stats = list()
    try:
        # Get the number of years from the user.
        years = int(input('Input the number of years of rain statistics' +
                          ' to use: '))

        # Get values for all months by using looping through the years
        for year in range(1, years + 1):
            print('\nValues for year {}'.format(year))
            stats.append(get_rain_year())
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Print final statistics.
    total_months = len(stats) * 12
    print('\nNumber of month in the period: {}'.format(total_months))

    #Calculate total rainfall
    total_rainfall = 0
    for year in range(0, years):
        for month in range(0, 12):
            total_rainfall += stats[year][month]

    print('Total rainfall for the period (in inches): ' +
          '{:0.2f}'.format(total_rainfall))
    print('Avarage rainfall for the period (in inches): ' +
          '{:0.2f}'.format(total_rainfall/total_months))

# Run this when invoked directly
if __name__ == '__main__':
    main()
