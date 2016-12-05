#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 1
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Program that keeps a running total of the number of bugs collected during the
seven days
'''
def main():
    '''
    Main entry point.
    '''
    # Get bugs each day.
    bugs = 0
    try:
        for day in range(1,8):
            print('Input the number of bugs for day {} '.format(day) +
                  '({} in total until now): '.format(bugs), end='')
            bugs += int(input())
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print('\nTotal bugs collected during the seven days: {}.'.format(bugs))


# Run this when invoked directly
if __name__ == '__main__':
    main()
