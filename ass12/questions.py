#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 8 "Trivia Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Class that encapsulates trivia questions.
"""
from ass12.question import Question


class Questions:
    """
    Class that holds trivia questions.
    """

    def __init__(self, file_name=None):
        """
        Constructor.

        :param file_name: File name to read the questions from.
        """
        self.__questions = list()

        # Read the questions from the input file.
        # Handle IO errors and conversion errors using excaptions.
        try:
            with open(file_name, 'r') as data_file:
                # Read every line until the end of the file.
                # This actually ends up reading a chunk of 6 lines during each
                # iteration.
                for line in data_file:
                    # First line is the question.
                    q = Question()
                    q.set_text(line)

                    # Next 4 line are the answers.
                    q_answers = list()
                    line = data_file.readline().strip()
                    if line != '':
                        q_answers.append(line.strip())
                    line = data_file.readline().strip()
                    if line != '':
                        q_answers.append(line.strip())
                    line = data_file.readline().strip()
                    if line != '':
                        q_answers.append(line.strip())
                    line = data_file.readline().strip()
                    if line != '':
                        q_answers.append(line.strip())
                        q.set_answers(q_answers)

                    # Last line is the answer.
                    line = data_file.readline().strip()
                    if line != '':
                        q.set_answer(int(line.strip()))
                        # Add the question, now that we've read it without
                        # failure.
                        self.__questions.append(q)

        except IOError as ex:
            # Complain when something goes wrong with the file access.
            print('Exception: {}'.format(str(ex)))
            print('Error loading quiz questions.')
            exit(1)
        except ValueError:
            # Something wrong with the contents if the file.
            print('Wrong format of input file.')
            exit(1)

    def get_question(self, number):
        """
        Get a specific question.

        :param number: The question number.
        :return: Question object.
        """
        return self.__questions[number]

    def get_questions(self):
        """
        Get a list of all questions.

        :return: List of Question ojects.
        """
        return self.__questions
