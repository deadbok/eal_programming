#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4 "Employee Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-01)

Class that encapsulates the properties of an employe.
"""


class Employee:
    """
    Employee class.
    """

    def __init__(self, name='John Doe', id='', department='', title=''):
        """
        Constructor.

        :param name: The name of the employee. Defaults to 'John Doe'.
        :param id: The ID number of the employee.
        :param department: The department that the employee is working in.
        :param title: The job title of the employee.
        """
        # Set to the values passed to the constructor.
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title

    def get_name(self):
        """
        Get the name.

        :return: The name
        """
        return self.__name

    def get_id(self):
        """
        Get the id.

        :return: The id
        """
        return self.__id

    def get_department(self):
        """
        Get the department.

        :return: The department
        """
        return self.__department

    def get_title(self):
        """
        Get the title.

        :return: The title
        """
        return self.__title

    def set_name(self, name):
        """
        Set the name.
        """
        self.__name = name

    def set_id(self, id):
        """
        Set the id.
        """
        self.__id = id

    def set_department(self, department):
        """
        Set the department.
        """
        self.__department = department

    def set_title(self, title):
        """
        Set the title.
        """
        self.__title = title

    def __str__(self):
        """
        Return a string with the value of the year models and make.
        :return:
        """
        return ('Employee')
