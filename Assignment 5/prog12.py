#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 12 "Rock, Paper, Scissors Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-10)

Rock, Paper, Scissors Game against the awesome AI that is the "random" number
generator.
"""
import random


def computerChoice():
    """
    Get the computer's choice.

    :return: Rock = 1, Paper = 2, Scissors = 3
    """
    return (random.randrange(1, 3))


def userChoice():
    """
    Get the user's choice.

    :return: A string with the users choice
    """
    # Get the users choice and convert to lower case, to catch some more
    # permutations.
    return (input('Input a choice of rock, paper, scissors: ').lower())

def getWinner(computer, user):
    """
    Find a winner.

    :param computer: The computers object choice.
    :param user: The users object choice.
    :return: Computer og You or None depending on who wins.
    """
    #No one wins by default.
    winner = None

    # Computer chooses rock, user scissors, computer wins
    if computer == 1 and user == 3:
        winner = 'Computer'
    # Computer chooses scissors, user paper, computer wins
    if computer == 3 and user == 2:
        winner = 'Computer'
    # Computer chooses paper, user rock, computer wins
    if computer == 2 and user == 1:
        winner = 'Computer'

    # User chooses rock, computer scissors, computer wins
    if user == 1 and computer == 3:
        winner = 'Computer'
    # User chooses scissors, computer paper, computer wins
    if user == 3 and computer == 2:
        winner = 'Computer'
    # User chooses paper, computer rock, computer wins
    if user == 2 and computer == 1:
        winner = 'Computer'

    return winner


def main():
    '''
    Program main entry point.
    '''
    # Crate a lookup list for the object types.
    objectNumbers = {1: 'rock', 2: 'paper', 3: 'scissors'}
    objectStrings = {'rock': 1, 'paper': 2, 'scissors': 3}

    winner = None
    # Repeat until someone wins.
    while winner is None:
        # Get computers choice.
        computerObject = computerChoice()
        # Get users choice and convert it into a number.
        try:
            userObject = objectStrings[userChoice()]
        except KeyError:
            # Complain when something unexpected was entered.
            print('\nPlease input either rock, paper, or scissors.')
            exit(1)

        print("The computer's choice is: {}".format(objectNumbers[computerChoice()]))

        winner = getWinner(computerObject, userObject)
        if winner is None:
            print('\nNo winner, have another go...\n')

    print('\nThe winner is: {}!'.format(winner))



# Run this when invoked directly
if __name__ == '__main__':
    main()
