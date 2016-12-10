#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Print distance travelled at a given speed at a given number of hours.
"""
def get_distance(hours=1, mph=40):
    '''
    Get ditance travelled at a certain speed after a certain number of hours.

    :param hours: Number of hours.
    :param mph: Miles per hour
    :return: Distance travelled
    '''
    # Calculate the total distance.
    return float(mph * hours)


def main():
    '''
    Program main entry point.
    '''
    # Get hours and mph from the user.
    hours = 0
    mph = 0
    try:
        mph = float(input('Input the speed of the vehichle in MPH: '))
        hours = int(input('Input hours travalled by the vehichle: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Print header.
    print('Hour\tDistance traveled')
    print('-------------------------')
    # Print a table of distance travelled at a certain number of housr of
    # travel
    for hours in range(1, hours + 1):
        #Print result.
        print('{:4}\t'.format(hours) +
              '{:12.2f}'.format(get_distance(hours)))

# Run this when invoked directly
if __name__ == '__main__':
    main()