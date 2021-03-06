#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 9
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-11)

A program that uses nested loops to draw this pattern:

    *******
    ******
    *****
    ****
    ***
    **
    *
'''


def main():
    '''
    Program main entry point.
    '''
    # Loop for the height.
    for h in range(0, 7):
        # Loop for the width.
        for w in range(0, 7 - h):
            # Print the characters of the shape.
            print('*', end='')
        # New line.
        print()


# Run this when invoked directly
if __name__ == '__main__':
    main()
