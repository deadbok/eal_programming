#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 9 "Rock, Paper, Scissors Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-15)

A program that lets the user enter the name of a team and then displays the
number of times that team has won the World Series in the time period from 1903
through 2009.
"""
import random


def load_winners(filename='WorldSeriesWinners.txt'):
    """
    Load the World Series winnin data from a file.

    :return: Dictionary of winners and years.
    """
    print('Loading winner data...')
    winners = dict()
    try:
        # Keep track of the year.
        year = 1903
        # Open 'numbers.txt' for reading.
        with open(filename, 'r') as data_file:
            # Run until 2010
            while (year < 2010):
                # Skip 1904 and 1994
                if (year != 1904) and (year != 1994):
                    # Get the team from the file remove new lines and convert to
                    # lower case to facilitate later matching.
                    team = data_file.readline().strip().lower()
                    print('\t{}:\t{}'.format(year, team.title()))
                    if team in winners.keys():
                        # The team is here update the list with current year.
                        winners[team].append(year)
                    else:
                        # Team is not here create a new list for the winning
                        # years
                        winners[team] = [year]
                year += 1

    except IOError as ex:
        # Complain when something goes wrong with the file access.
        print('Exception: {}'.format(str(ex)))
        print('Error loading winners.')
        exit(1)
    print('OK\n')
    return (winners)


def get_team(winners):
    """
    Get the the team to get the wins for.

    :return: The name that the user selected.
    """

    def list_teams():
        """
        List all team names in the winners dictionary.
        """
        # Counter for the output
        i = 1
        # Print eac team
        for team in teams:
            print(
                '{}:\t{} ({})'.format(i, team.title(), len(winners[team])))
            i += 1

    # List of all team names
    teams = [winner for winner in winners]
    try:
        # Ask for the sales figure for each day.
        team = int(input(
            '\nEnter a number of the team (-1 to quit, 0 to list teams): '))
        # Give the user a chance to get out.
        if team == -1:
            # Signal that we want out.
            return (None)
        # List team names.
        if team == 0:
            list_teams()
            # Select team.
            return get_team(winners)

        # Adjust for indexing the list
        team -= 1
        print('\t{} selected.'.format(teams[team].title()))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.\n')
        # Select team.
        return get_team(winners)
    except IndexError:
        # The index was not in the list
        print('\nTeam not found.\n')
        list_teams()
        # Select team.
        return get_team(winners)

    return (teams[team])


def print_team_info(team, years):
    """
    Print the number of wins and the winning years of a team.

    :param team: The name of the team.
    :param years: A list of ears the team has won.
    """
    # Create a comma seperated list of the years in a string
    year_str = ','.join(['{:5}'.format(year) for year in years])
    # Print the numbers.
    if len(years) > 1:
        print('\n{} has {} victories in the years:{}'.format(team.title(),
                                                             len(years),
                                                             year_str))
    else:
        print('\n{} has {} victory in: {}'.format(team.title(), len(years),
                                                  year_str))


def main():
    '''
    Program main entry point.
    '''
    # Load the data
    winners = load_winners()
    # Select a team.
    team = get_team(winners)
    # Keep going until the user says stop.
    while team is not None:
        # Print team info
        print_team_info(team, winners[team])
        # Select team
        team = get_team(winners)

    print('\nBye.')


# Run this when invoked directly
if __name__ == '__main__':
    main()
