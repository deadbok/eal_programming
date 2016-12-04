#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 5
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Calculate the assessment value and property tax from the actual value of a piece
of property
"""
def assessment_value(value = 0):
    """
    Calculate the assessment value (60%) from the actual value.

    :param value: The actual value of the property.
    :return: The assessment value.
    """
    # Return the assessment value.
    return(value * 0.6)


def property_tax(value=0):
    """
    Calculate the property tax (0.64%) from the actual value.

    :param value: The actual value of the property.
    :return: The assessment value.
    """
    # Return the property tax value.
    return(assessment_value(value) * 0.0064)


def main():
    """
    Program main entry point.
    """
    # Get the value of the property from the user.
    try:
        value = float(input('Enter the value of the property: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print('\nProperty value:\t\t{:12.2f}'.format(value))
    print('Assessment value:\t{:12.2f}'.format(assessment_value(value)))
    print('Property tax:\t\t{:12.2f}'.format(property_tax(value)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
