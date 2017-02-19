#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Employee and ProductionWorker Classes"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-12)

Class that simulates a cash register.
"""

class CashRegister:
    """
    CashRegister class.
    """

    def __init__(self):
        """
        Constructor.
        """

        # List holding the items selected for purchase.
        self.__cart = list()

    def purchase_item(self, new_item):
        """
        Purchase an item.

        :param item: A RetailItem.
        """
        # Add the item to the cart.
        # Run through all items and ask each to add it, if it is the owner.
        i = 1
        found = False
        if len(self.__cart):
            found = self.__cart[0].add_item(new_item.get_description())
            while not found and (len(self.__cart) > i):
                found = self.__cart[i].add_item(new_item.get_description())
                i += 1

        # No similar RetailItem was in the cart, add this one.
        if not found:
            self.__cart.append(new_item)


    def get_total(self):
        """
        Get the total price of the items in the cart.

        :return: Total price of items in the cart.
        """
        ret = 0
        for item in self.__cart:
            ret += item.get_price() * item.get_inventory()

        return(ret)

    def show_items(self):
        """
        Print all items in the cart.
        """
        # Print the items in a table, first the header.
        print('\n------------------------------------------------------' +
              '-----------')
        print('| #         | Description          | Units in cart |' +
              ' Price      |')
        print('------------------------------------------------------' +
              '-----------')
        # Print the items.
        for i in range(len(self.__cart)):
            item = self.__cart[i]
            print(
                '| Item {:4} | {:>20} |'.format(i + 1, item.get_description()),
                end='')
            print(' {:13.0f} | {:10.2f} |'.format(item.get_inventory(),
                                                  item.get_price() * item.get_inventory()))

        # Handle empty table.
        if not len(self.__cart):
            print(
                '| No items                                        ' +
                '              |')
        # Close the table.
        print('-------------------------------------------------------' +
              '----------')
        print('Total price: {:10.2f}'.format(self.get_total()))

    def clear(self):
        """
        Clear the cart.
        """
        self.__cart = list()
