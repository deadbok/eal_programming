#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 2 "ShiftSupervisor Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Class that encapsulates the properties of a shift supervisor.
"""
from ass14.employee import Employee


class ShiftSupervisor(Employee):
    """
    ShiftSupervsior class.
    """

    def __init__(self, name='John Doe', number=0, annual_pay=0, annual_bonus=0):
        """
        Constructor.

        :param name: The name of the employee. Defaults to 'John Doe'.
        :param number: The number of the employee.
        :param annual_sallery: Annual sallery of the employee.
        :param annual_bonus: Annual bonus of the employee.
        """
        # Call the parent constructor.
        Employee.__init__(self, name, number)
        # Set to the values passed to the constructor.
        self.__annual_pay = annual_pay
        self.__annual_bonus = annual_bonus

    def get_annual_pay(self):
        """
        Get the annual pay.

        :return: The annual pay
        """
        return self.__annual_pay

    def get_annual_bonus(self):
        """
        Get the annual bonus.

        :return: The annual bonus.
        """
        return self.__annual_bonus

    def set_annual_pay(self, pay):
        """
        Set the sannual pay.
        """
        self.__annual_pay = pay

    def set_annual_bonus(self, bonus):
        """
        Set the annual onus.
        """
        self.__annual_bonus = bonus

    def __str__(self):
        """
        Return a string representing the object.

        :return: string
        """
        return ('Shift supervisor "{}", number {}'.format(self.get_name(),
                                                          self.get_number()) +
                ', annual sallery {}'.format(self.get_annual_pay()) +
                ', annual bonus {}'.format(self.get_annual_bonus()))
