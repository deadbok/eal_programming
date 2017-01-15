#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2 "Math Quiz"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-10)

Calculate the sum of numbers input by the user.
'''
import random


def print_puzzle():
    """
    Print an addition puzzle.

    :return: The result of the addition.
    """
    # Generate the numbers to add, limit the max value to 1000
    # Convert them to string and truncate them, to avoid later rounding errors.
    firstNumber = '{:7.2f}'.format(random.randrange(1, 1000))
    secondNumber = '{:7.2f}'.format(random.randrange(1, 1000))

    # Output the puzzle.
    print('   ' + firstNumber)
    print(' + ' + secondNumber)
    print('-' * 11)

    return float(firstNumber) + float(secondNumber)


def get_user_result():
    """
    Get the result from the user.

    :return: User result.
    """
    try:
        return (float(input('\nInput you answer: ')))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)


def main():
    '''
    Program main entry point.
    '''
    print('Do the following math puzzle: \n\n')
    result = print_puzzle()
    userResult = get_user_result()
    print()

    if (result != userResult):
        print('The correct answer is {:.2f}'.format(result))
    else:
        print('Congratulations, your answer was correct!')


# Run this when invoked directly
if __name__ == '__main__':
    main()
