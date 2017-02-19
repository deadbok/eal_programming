#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 8 "Trivia Game"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Class that encapsulates q trivia question.
"""


class Question:
    """
    Class that holds personal information.
    """

    def __init__(self, text='None', answers=[], answer=0):
        """
        Constructor.

        :param text: The question.
        :param answers: A list of answer strings.
        :param answer: Number of the correct answer.
        """
        self.__text = text
        self.__answers = answers
        self.__answer = 1

    def get_text(self):
        """
        Get the question.

        :return: The question.
        """
        return self.__text

    def get_answers(self, number = None):
        """
        Get the answers.

        :param number: If set only, return the specific question.
        :return: List of answers.
        """
        ret = self.__answers

        if (number > 0) and (number < 5):
            ret = self.__answers[number - 1]

        return ret

    def get_answer(self):
        """
        Get the number of the correct answer.

        :return: The number of the correct answer.
        """
        return self.__answer

    def set_text(self, text):
        """
        Set the question.

        :param text: String with the question.
        """
        self.__text = text

    def set_answers(self, answers):
        """
        Set the possible answers.

        :param answers: List of answers.
        """
        if len(answers) == 4:
            self.__answers = answers
        else:
            print('Error: Exactly 4 answers are required')

    def set_answer(self, answer):
        """
        Set the number of the correct answer.

        :param answer: The number of the correct answer.
        """
        if (answer > 0) and (answer < 5):
            self.__answer = answer
        else:
            print('Answer is out of range.')
