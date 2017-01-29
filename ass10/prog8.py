#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 8 "Name and Email Addresses"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-29)

Program to organise name and email addresses.
"""
from app import App


def main():
    """
    Program main entry point.
    """
    # Instantiate the application class.
    app = App('test.db')
    # Start the application main loop.
    app.run()


# Run this when invoked directly
if __name__ == '__main__':
    main()
