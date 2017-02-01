#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Pet Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-01)

Program to organise name and email addresses.
"""
class Pet:
    """
    Pet class, holds the name, type, and age of a pet.
    """
    def __init__(self, name='', animal_type=None, age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        """
        Set the name of the pet.
        :param name: The name
        """
        self.name = name

    def set_animal_type(self, type):
        """
        Set the type of the pet.

        :param type: The type of pet.
        """
        self.__animal_type = type

    def set_age(self, age):
        """
        Set the age of the pet.

        :param age: Age og the pet.
        """
        self.__age = age

    def get_name(self):
        """
        Get the name of the pet.

        :return: The name of the pet.
        """
        return self.__name

    def get_type(self):
        """
        Get the type of the pet.

        :return: The type of the pet.
        """
        return self.__animal_type

    def get_age(self):
        """
        Get the age of the animal.

        :return: The age of the pet.
        """
        return self.__age

    def __str__(self):
        return('Name: {}\nType: {}\nAge: {}'.format(self.__name, self.__animal_type, self.__age))
