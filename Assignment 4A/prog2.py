#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Display the number of calories burned after 10, 15, 20, 25, and 30
minutes.
'''
def get_calories_burned(minutes=1, cal_per_min=3.9):
    '''
    Get the calories burned for a certain amount of minutes.

    :param minutes: Number of minutes.
    :param cal_per_min: Calories burned per minute.
    :return: Caloties burned.
    '''
    # Calculate the total calories
    return float(cal_per_min * minutes)


def main():
    '''
    Program main entry point.
    '''
    # Run from 10 to 30 adding 5 each time around.
    for minutes in range(10, 31, 5):
        #Print result.
        print('Calories burned after {} minutes: '.format(minutes) +
              '{:0.2f}'.format(get_calories_burned(minutes)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
