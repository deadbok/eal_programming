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
from question import Question

class Questions:
    """
    Class that holds trivia questions.
    """
    def __init__(self, file_name = None):
        """
        Constructor.

        :param file_name: File name to read the questions from.
        """
        self.__questions = list()

        try:
            with open(file_name, 'r') as data_file:
                q_text = data_file.readline().strip()
                while q_text != '':
                    q_answer1 = data_file.readline().strip()

                for line in data_file:

                    # Strip line endings
                    line.strip())
        except IOError as ex:
            # Complain when something goes wrong with the file access.
            print('Exception: {}'.format(str(ex)))
            print('Error loading text.')
            exit(1)
