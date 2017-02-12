#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 2 "ShiftSupervisor Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Program that tests the ShiftSupervisor class
"""
from ass12.shiftsupervisor import ShiftSupervisor


def main():
    """
    Program main entry point.
    """
    # Instantiate the ShiftSupervisor class.
    my_ss = ShiftSupervisor(name='Hans Hansen')

    #Set the values.
    my_ss.set_number(1)
    my_ss.set_annual_bonus(50000)
    my_ss.set_annual_pay(500000)

    # Print the data.
    print(str(my_ss))

# Run this when invoked directly
if __name__ == '__main__':
    main()
