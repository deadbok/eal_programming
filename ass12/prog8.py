#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 8 "Trivia Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

A Trivia game.
"""
from ass12.quiz import Quiz


def main():
    """
    Program main entry point.
    """
    # Create a game for 2 players.
    prog_quiz = Quiz(2, 'triviaQuestionsChap11.txt')
    # Run the game.
    prog_quiz.run()
    # Print the results.
    prog_quiz.print_results()


# Run this when invoked directly
if __name__ == '__main__':
    main()
