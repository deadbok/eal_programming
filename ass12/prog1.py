#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Employee and ProductionWorker Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Program for entering details in to a ProductionWorker class.
"""
from ass12.productionworker import ProductionWorker


def main():
    """
    Program main entry point.
    """
    # Instantiate the ProductionWorker class.
    my_pw = ProductionWorker()

    try:
        # Use the setters, to set the values from user input.
        my_pw.set_name(input('Input the name of the employee: '))
        my_pw.set_number(int(input('Input the numer of the employee: ')))
        shift = str(input(
            'Input the shift the employee is assgined to (day, night): '))
        shift = shift.upper()
        # Validate the shift value.
        if shift in ['DAY', 'NIGHT']:
            if shift == 'DAY':
                my_pw.set_shift(ProductionWorker.DAY)
            else:
                my_pw.set_shift(ProductionWorker.NIGHT)
        else:
            raise ValueError
        my_pw.set_hourly_pay(
            int(input('Input the hourly pay of the employee: ')))

    except ValueError:
        # Complain when something unexpected was entered.
        print('\nThe input was wrong.')
        exit(1)

    print('\nYou entered: ')
    # There are cleaner ways, but I'm asked to use the setter/getter here.
    print(' Name:\t\t\t{}'.format(my_pw.get_name()))
    print(' Number:\t\t{}'.format(my_pw.get_number()))
    print(' Shift:\t\t\t{}'.format(my_pw.get_shift_str()))
    print(' Hourly pay:\t{}'.format(my_pw.get_hourly_pay()))


# Run this when invoked directly
if __name__ == '__main__':
    main()
