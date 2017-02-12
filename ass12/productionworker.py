#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Employee and ProductionWorker Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Class that encapsulates the properties of a production worker.
"""
from ass12.employee import Employee


class ProductionWorker(Employee):
    """
    ProductionWorker class.
    """
    DAY = 1
    NIGHT = 2

    def __init__(self, name='John Doe', number=0, shift=0, hourly_pay=0):
        """
        Constructor.

        :param name: The name of the employee. Defaults to 'John Doe'.
        :param number: The number of the employee.
        :param shift: The shift that the employee is on.
        :param hourly_pay: The hourly pay that the worker earns.
        """
        # Call the parent constructor.
        Employee.__init__(self, name, number)
        # Set to the values passed to the constructor.
        self.__shift = shift
        self.__hourly_pay = hourly_pay

    def get_shift(self):
        """
        Get the shift.

        :return: The shift
        """
        return self.__shift

    def get_shift_str(self):
        """
        Get the shift as a string.

        :return: The shift as a string.
        """
        ret = 'unknown'
        if self.__shift is ProductionWorker.DAY:
            ret = 'day'
        elif self.__shift is ProductionWorker.NIGHT:
            ret = 'night'

        return ret

    def get_hourly_pay(self):
        """
        Get the hourly pay.

        :return: The hourly pay
        """
        return self.__hourly_pay

    def set_shift(self, shift):
        """
        Set the shift.
        """
        self.__shift = shift

    def set_hourly_pay(self, hourly_pay):
        """
        Set the hourly pay.
        """
        self.__hourly_pay = hourly_pay

    def __str__(self):
        """
        Return a string representing the object.

        :return: string
        """
        return ('ProductionWorker "{}", number {}'.format(self.get_name(),
                                                          self.get_number()) +
                ', shift {}, hourly pay {}'.format(self.get_shift_str(),
                                                   self.get_hourly_pay()))
