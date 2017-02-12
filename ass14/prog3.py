#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Person and Customer Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Program that uses the Customer class.
"""
from ass14.customer import Customer

def main():
    """
    Program main entry point.
    """
    # Create a list of people.
    new_cus = Customer()

    #Create a customer.
    new_cus.set_name('Hans Hansen')
    new_cus.set_address('Hans Hansensvej 555, 8210 Aarhus V')
    new_cus.set_phone('1231456')
    new_cus.set_number(500)
    new_cus.set_receive_mail()

    #Print.
    print(new_cus)

    print('\nRemoving customer form mailing list\n')

    new_cus.set_receive_no_mail()
    print(new_cus)

# Run this when invoked directly
if __name__ == '__main__':
    main()
