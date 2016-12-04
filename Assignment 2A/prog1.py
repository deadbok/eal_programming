#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Convert kilometres to miles.
'''
def km2miles(kilometres = 0):
    '''
    Convert kilometres to miles.

    :param kilometres: Distance in kilometres.
    :return: Distance in miles.
    '''
    #Code that converts km to miles
    return(kilometres * 0.6214)


def main():
    '''
    Main entry point.
    '''
    # Get the amount of kilometres from the user.
    try:
        kilometres = float(input('Input kilometres: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print('{:0.2f} kilometres is {:0.2f} miles'.format(kilometres, km2miles(kilometres)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
