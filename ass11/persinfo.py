#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Personal Information Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-01)

Class that encapsulates personal information.
"""

# Design a class that holds the following personal data: name, address, age, and
# phone number. Write appropriate accessor and mutator methods.

class PersonalInfo:
    """
    Class that holds personal information.
    """
    def __init__(self, name='John Doe', address='', age=0, phone=''):
        """
        Constuctor.

        :param name: The name of the person. Default is 'John Doe'.
        :param address: The address of the person.
        :param age: The age of the person. Default is 0.
        :param phone: The phone number of the person.
        """
        # Set to the values passed to the constructor.
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_name(self):
        """
        Get the name.

        :return: The name.
        """
        return self.__name

    def get_address(self):
        """
        Get the address

        :return: The address
        """
        return self.__address

    def get_age(self):
        """
        Get the age

        :return: The age
        """
        return self.__age

    def get_phone(self):
        """
        Get the phone number.

        :return: The phone number
        """
        return self.__phone

    def set_name(self, name):
        """
        Set the name.
        """
        self.__name = name

    def set_address(self, address):
        """
        Set the address
        """
        self.__address = address

    def set_age(self, age):
        """
        Set the age
        """
        self.__age = age

    def set_phone(self, phone):
        """
        Set the phone number.
        """
        self.__phone = phone

    def __str__(self):
        """
        Return a string that is directly usable when printing the entry.
        :return:
        """
        return('Name:\t\t{}\n'.format(self.__name) +
               'Age:\t\t{}\n'.format(self.__age) +
               'Address:\t{}\n'.format(self.__address) +
               'Phone:\t\t{}\n'.format(self.__phone))
