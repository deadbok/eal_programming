#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 8 "Trivia Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Class that handles the general quiz logic.
"""
import random

from ass12.questions import Questions


class Quiz:
    """
    Quiz class.
    """

    def __init__(self, players, data_file_path):
        """
        Constructor.

        :param players: Number of players.
        :param data_file_path: Text file to read the questions and answers from.
        """
        self.__questions = Questions(data_file_path)
        self.__players = players
        self.__answers = list()

    def run(self):
        """
        Run a the quiz.
        """
        n_questions = len(self.__questions.get_questions())

        for player in range(self.__players):
            print('\nQuestions for player {}'.format(player + 1))
            print('----------------------\n\n')

            n_answered = list()
            i = 0
            for i in range(5):
                print('Question {}:'.format(i + 1))
                print('-----------\n')
                number = random.randrange(0, n_questions)
                # If question is answered find a new one.
                # If question choices are exhausted this will go into an
                # endless loop.
                while number in [a[0] for a in n_answered]:
                    number = random.randrange(0, n_questions)

                # Print question.
                current_question = self.__questions.get_question(number)
                print(current_question.get_text())
                # Print answers.
                for j in range(4):
                    print(' {}: {}'.format(j + 1,
                                           current_question.get_answers(j + 1)))

                # Get the user answer.
                u_answer = 0
                while not u_answer:
                    try:
                        u_answer = int(
                            input('\nEnter the number of the correct answer: '))
                        if (u_answer < 1) or (u_answer > 4):
                            raise ValueError
                    except ValueError:
                        print('\n*Please use only numbers 1, 2, 3, and 4.*\n')
                        u_answer = 0

                # Add to answered questions.
                n_answered.append((number, u_answer))

                print()

            # Save the players answers.
            self.__answers.append(n_answered)

    def print_results(self):
        """
        Print the results of a game.
        """
        # For all players
        for player in range(self.__players):
            print('\nResults for player {}'.format(player + 1))
            print('----------------------\n\n')

            # All answers.
            i = 1
            correct = 0
            for answer in self.__answers[player]:
                print('Question {}:'.format(i))
                print('------------\n')
                # ¿Que?
                que = self.__questions.get_question(answer[0])
                # Print question, answer, and correct answer.
                print(que.get_text())
                print('Answer: ' +
                      format(que.get_answers(answer[1])))
                print('Correct answer: ' +
                      format(que.get_answers(que.get_answer())))
                if que.get_answer() == answer[1]:
                    print('\nAnswer is correct.')
                    correct += 1
                else:
                    print('\nAnswer is wrong.')

                # Next question.
                i += 1

                print()

        # Print final scores for all players.
        for player in range(self.__players):
            print('Player {}: {} answer(s) of 5 correct.'.format(player + 1,
                                                                 correct))
