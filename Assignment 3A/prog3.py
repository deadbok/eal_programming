#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 3
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (19/11-2016)

Calculate the weight of an object in newtons, warn if the object is lighter
than 10 newtons or heavier than 1000 newtons.
'''
def get_weight(mass=1):
    """
    Get the weight in newtons from the mass in kilograms.

    :param mass: Mass in kilograms.
    :return: Weight in newtons.
    """
    return(mass * 9.8)


def main():
    '''
    Program main entry point.
    '''
    # Get the amount of purchase from the user.
    try:
        mass = float(input('Enter the mass of the object in kilograms: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Calculate the weight.
    weight = get_weight(mass)
    # Print it.
    print('\nAn object with a mass of {:0.2f} kilograms'.format(mass) +
          ' has a weight of {:0.2f} newtons.'.format(weight))

    # Print a warning if object is larger or smaller than the min, max values.
    if weight > 1000:
        print('Warning: the object is heavier than 1000 newtons')
    if weight < 10:
        print('Warning: the object is lighter than 10 newtons')


# Run this when invoked directly
if __name__ == '__main__':
    main()
