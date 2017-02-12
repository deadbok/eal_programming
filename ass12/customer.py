#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Personal Information Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Class that encapsulates the properties of a customer.
"""
from ass12.person import Person


class Customer(Person):
    """
    Customer class.
    """
    def __init__(self, name='John Doe', address='', phone='', number=0,
                 mail=False):
        """
        Constuctor.

        :param name: The name of the customer. Default is 'John Doe'.
        :param address: The address of the customer.
        :param phone: The phone number of the customer.
        :param number: The customer number.
        :param mail: True is the customer is on the mailing list.
        """
        # Call the parent constructor.
        Person.__init__(self, name, address, phone)
        # Set to the values passed to the constructor.
        self.__number = number
        self.__mail = mail

    def get_number(self):
        """
        Get the customer number.

        :return: The scustomer number.
        """
        return self.__number

    def get_receive_mail(self):
        """
        True if the customer is on the mailing list.

        :return: The mailing list status.
        """
        return self.__mail

    def get_receive_mail_str(self):
        """
        Return the customer the mailing list status. 'yes' if the customer
        receives mail, 'no' otherwise.

        :return: The mailing list status.
        """
        ret = False
        if self.__mail:
            ret = True
        return ret

    def set_number(self, number):
        """
        Set customer number.
        """
        self.__number = number

    def set_receive_mail(self, mail):
        """
        Set whether or not the customer receives mail.
        """
        self.__mail = mail

    def __str__(self):
        """
        Return a string that is directly usable when printing the entry.

        :return: string
        """
        return('Name:\t\t{}\n'.format(self.get_name()) +
               'Address:\t\t{}\n'.format(self.get_address()) +
               'Phone:\t\t{}\n'.format(self.get_phone()) +
               'Number:\t\t{}\n'.format(self.get_number()) +
               'Is on the mailing list:\t{}'.format(self.get_receive_mail_str())
               )
