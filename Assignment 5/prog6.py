#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 6 "Test Average and Grade"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-10)

Convert 5 grades from numbers into letter.
"""


def calc_average(grade1, grade2, grade3, grade4, grade5):
    """
    Return the avarage of 5 scores.

    :param grade1: Grade 1
    :param grade2: Grade 2
    :param grade3: Grade 3
    :param grade4: Grade 4
    :param grade5: Grade 5
    :return: The average grade as a number.
    """
    # Return the average.
    return (grade1 + grade2 + grade3 + grade4 + grade5) / 5


def determine_grade(score):
    """
    Return the letter score using the following conversion
    table:

     Score    | Letter Grade
    ----------|---------------
     90–100   | A
     80–89    | B
     70–79    | C
     60–69    | D
     Below 60 | F

    :param score: The numerical score.
    :return: The letter score.
    """
    # Be !positive and return 'F' by default.
    ret = 'F'
    # Use if to convert to letter score.
    if score >= 90:
        ret = 'A'
    elif score >= 80:
        ret = 'B'
    elif score >= 70:
        ret = 'C'
    elif score >= 60:
        ret = 'D'

    return ret


def get_grade():
    """
    Get the one grade from the user.

    :return: The grade.
    """
    try:
        return (float(input('Input a numerical score (0-100): ')))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)


def main():
    """
    Program main entry point.
    """
    # Handle the input in a list.
    scores = list()
    for i in range(5):
        scores.append(get_grade())

    # I would much rather have passed the list, but the assignment says
    # otherwise.
    average = calc_average(scores[0], scores[1], scores[2], scores[3],
                           scores[4])

    # Print the input scores and their letter scores.
    print('\nScores: ')
    for score in scores:
        print(' {:6.2f}: {}'.format(score, determine_grade(score)))
    # Print the average.
    print(
        '\nAverage score {:0.2f}: {}'.format(average, determine_grade(average)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
