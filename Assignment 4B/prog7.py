#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 7
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-10)

Calculate the amount of money a person would earn over a period of time if his
or her salary is one penny the first day, exponentially rising each day.
'''


def grow_or_pay(pay=1, days=2, day=1, total=0):
    '''
    Calculate the amount of pay, doubling the sallery each day.

    :param pay: The sallary to base the calculation on.
    :param days: The number of days to calculate the salary for,
    :param day: The current day.
    :return: The total salary.
    '''
    # Print the current results.
    print('{:12.2f}\t|{:4d}\t|{:16.2f}'.format(pay, day, total))

    # Check if we're done.
    if days == day:
        return (pay)

    # Next step.
    pay *= 2
    total += pay
    day += 1

    # Call again.
    return (grow_or_pay(pay, days, day, total))


def main():
    '''
    Main entry point.
    '''
    # Get number of days, and salary from the user.
    days = 0
    pay = 0
    try:
        pay = float(input('Input the amount of sallery per day: '))
        days = int(input('Input the amount of days: '))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    print('\nDaily salery\t| Day\t|\tTotal salery')
    print('------------------------------------------')
    total_pay = grow_or_pay(pay, days)
    print('------------------------------------------')
    total_pounds = int(total_pay / 100)
    total_pennies = total_pay - (total_pounds * 100)
    print('{:.2f} is {:.0f} pounds and {:2.0f} pennies'.format(total_pay,
                                                               total_pounds,
                                                               total_pennies))


# Run this when invoked directly
if __name__ == '__main__':
    main()
