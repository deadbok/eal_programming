#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 2 "Car Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-01)

Class that encapsulates the properties of a car.
"""


class Car:
    """
    Car class.
    """

    def __init__(self, year_model=0, make='Trabant'):
        """
        Constructor.

        :param year_model: Year of the model. Default is 0.
        :param make: Make of the cat. Default is Trabant.
        """
        # Set to the values passed to the constructor.
        self.__year_model = year_model
        self.__make = make
        # We're going no where.
        self.__speed = 0

    def accelerate(self):
        """
        Add some speed.
        """
        self.__speed += 5

    def brake(self):
        """
        Substract some speed.
        """
        self.__speed -= 5

    def get_speed(self):
        """
        Get the current speed of the car

        :return: The speed of the car.
        """
        return self.__speed

    def __str__(self):
        """
        Return a string with the value of the year model and make.
        :return:
        """
        return (' Year model:\t{}\n'.format(self.__year_model) +
                ' Make:\t{}\n'.format(self.__make))
