#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Personal Information Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Class that holds data about an item in a retail store.
"""

class RetailItem:
    """
    RetailItem class.
    """
    def __init__(self, description='None', inventory=0, price=0):
        """
        Initialise the retail item.

        :param description: The description of the item.
        :param inventory: The number of items in the inventory-
        :param price: The price of the item.
        """
        self.__description = description
        self.__inventory = inventory
        self.__price = price


    def get_description(self):
        """
        Get the item desciption.

        :return: String with item description.
        """
        return self.__description

    def get_inventory(self):
        """
        Get the number of items in the inventory.

        :return: The number of items.
        """
        return self.__inventory

    def get_price(self):
        """
        Get the price of the item.

        :return: The price of the item.
        """
        return self.__price

    def set_description(self, description):
        """
        Set the item description.

        :param description: The item description.
        """
        self.__description = description

    def set_inventory(self, inventory):
        """
        Set the number of items in the inventory.

        :param inventory: The number of items.
        """
        self.__inventory = inventory

    def set_price(self, price):
        """
        Set the price of the item.

        :param price: The proce of the item.
        """
        self.__price = price

    def add_item(self, description = None):
        """
        Helper function to add a new item to the inventory.
        If a description is supplied, the item description must match this
        for the item to get added.

        :param description: Item description.
        :return: True if added.
        """
        ret = False
        if description is None:
            self.__inventory += 1
            ret = True
        else:
            if description == self.get_description():
                self.__inventory += 1
                ret = True

        return ret

    def remove_item(self, description = None):
        """
        Helper function to remove an item.
        If a description is supplied, the item description must match this
        for the item to get removed.

        :param description: Item description.
        :return: True if removed.
        """
        ret = False
        if description is None:
            self.__inventory -= 1
            ret = True
        else:
            if description == self.get_description():
                self.__inventory -= 1
                ret = True

        return ret

    def __str__(self):
        """
        Return a string that is directly usable when printing the entry.

        :return: string
        """
        return('{:20}\t'.format(self.get_description()) +
               '{:8.2f}\t'.format(self.get_price())
               )
