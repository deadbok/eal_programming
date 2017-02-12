#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Person and Customer Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Program that uses a class to hold the personal information of a few people.
"""
from ass12.customer import Customer

def main():
    """
    Program main entry point.
    """
    # Create a list of people.
    new_cus = Customer()

    print(new_cus)


# Run this when invoked directly
if __name__ == '__main__':
    main()
