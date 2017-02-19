#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 7 "Cash Register"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Program that simulates a cash register with built in inventory keeping.
"""
from ass12.retailitem import RetailItem
from ass12.cashregister import CashRegister


class App:
    """
    This class takes care of the overall control and ui of the application.
    """
    # The key assignments for the menu.
    QUIT = 0
    BUY = 1
    PURCHASE = 2
    SHOW = 3
    CLEAR = 4

    def __init__(self, items=[]):
        """
        Create the application class.

        ;param items: List of RetailItems for sale.
        """
        # List of menu items, their numbers, and methods.
        self.menu_items = [
            (self.QUIT, ' {}: {}'.format(self.QUIT, 'Quit'), None),
            (self.BUY, ' {}: {}'.format(self.BUY, 'Add items to the cart'),
             self.buy),
            (self.PURCHASE, ' {}: {}'.format(self.PURCHASE,
                                             'Purchase items in the cart'),
             self.purchase),
            (self.SHOW, ' {}: {}'.format(self.SHOW,
                                         'Show all items in the cart'),
             self.show),
            (self.CLEAR, ' {}: {}'.format(self.CLEAR, 'Clear the cart'),
             self.clear)
        ]

        # Items for sale
        self.__sale_items = items

        # Cash register
        self.__register = CashRegister()

        # Currently no entry is selected.
        self.selected = None
        self.op = -1

    def menu(self):
        """
        Print the main menu.
        """
        # Print header and selection name.
        print('\nMain menu', end='')
        if self.selected is None:
            print(' (no entry selected):')
        else:
            print(' ({} selected): '.format(self.selected))

        # Print menu entries.
        for entry in self.menu_items:
            print(entry[1])

        # Print the data of the selected entry.
        if self.selected is not None:
            print('\nSelected: ')
            self.printEntry(self.selected, False)

    def select_op(self):
        """
        Present a menu and validate the user selection.
        """
        # Show the menu.
        self.menu()
        # Get the user choice.
        choice = input('\nSelect operation: ')
        # Blank line.
        print('')

        # Validate the user input.
        try:
            self.op = int(choice)
            # Check if the choice is within range.
            if (self.op < 0) or (self.op > len(self.menu_items)):
                raise ValueError
        except ValueError:
            print('Wrong input, please try again')
            # Call recursively, program dies if you do enough wrong choices,
            # because of this.
            self.select_op()

    def buy(self):
        """
        Add user selected items to the cart..
        """
        # Variable for the selected item.
        selected = 1
        # Keep running the menu until 0 is selected
        while selected:
            print('Select an item to add it to the cart.\n')

            # Print a list of the items
            i = 0
            for i in range(len(self.__sale_items)):
                print('{:2.0f}: {}'.format(i + 1, self.__sale_items[i]))

            try:
                # Get the item selection from the user
                selected = int(input('\nInput item to add (0 to stop): '))

                # Handle, quit, wrong item, and adding.
                if selected == 0:
                    print('\n*Leaving item selection.*\n')
                elif len(self.__sale_items) < (selected):
                    print('\n*Non existing item selected.*\n')
                else:
                    self.__register.purchase_item(
                        self.__sale_items[selected - 1])

            except ValueError:
                print('\n*Please use only numbers.*\n')

    def purchase(self):
        """
        Edit an entry.
        """
        print('\nThank you for your purchase.\n')
        self.__register.clear()

    def show(self):
        """
        Show all entries in the cart.
        """
        self.__register.show_items()

    def clear(self):
        """
        Clear the cart.
        """
        self.__register.clear()

    def run(self):
        """
        Run the application.

        """
        # Let the user select an operation.
        self.select_op()

        # Run until quit is selected.
        while self.op != 0:
            # Run the selected operation.
            self.menu_items[self.op][2]()
            # Let the user select an operation.
            self.select_op()

        print('Bye.')


def main():
    """
    Program main entry point.
    """
    # These are the items for sale.
    items = list()
    items.append(RetailItem('BC547 npn transistor', 1, 1.05))
    items.append(RetailItem('BC557 pnp transistor', 1, 1.15))
    items.append(RetailItem('10kOhm 1/4W resistor', 1, 0.25))
    items.append(RetailItem('1kOhm 1/4W resistor', 1, 0.25))
    items.append(RetailItem('10uF 16V capacitor', 1, 0.50))
    items.append(RetailItem('5mm red LED', 1, 1.00))

    # Create an application instance using the items.
    app = App(items)
    # Run it.
    app.run()


# Run this when invoked directly
if __name__ == '__main__':
    main()
