#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Employee and ProductionWorker Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Class that encapsulates the properties of an employe.
"""


class Employee:
    """
    Employee class.
    """

    def __init__(self, name='John Doe', number=0):
        """
        Constructor.

        :param name: The name of the employee. Defaults to 'John Doe'.
        :param number: The number of the employee.
        """
        # Set to the values passed to the constructor.
        self.__name = name
        self.__number = number

    def get_name(self):
        """
        Get the name.

        :return: The name
        """
        return self.__name

    def get_number(self):
        """
        Get the number.

        :return: The number
        """
        return self.__number

    def set_name(self, name):
        """
        Set the name.
        """
        self.__name = name

    def set_number(self, number):
        """
        Set the number.
        """
        self.__number = number

    def __str__(self):
        """
        Return a string representing the object.

        :return: string
        """
        return ('Employee "{}" number {}'.format(self.__name, self.__number))
