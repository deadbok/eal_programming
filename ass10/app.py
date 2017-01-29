# -*- coding: utf-8 -*-
"""
Name: Program 8 "Name and Email Addresses"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-29)

Program control and ui code.
"""
from data import Data


class App:
    """
    This class takes care of the overall control and ui of the application.
    """
    # The key assignments for the menu.
    QUIT = 0
    ADD = 1
    EDIT = 2
    DEL = 3
    SEARCH = 4
    LIST = 5
    SELECT = 6

    def __init__(self, db_file_name):
        """
        Create the application class.

        :param db_file_name: The name of the file to pickle the data to and
                             from.
        """
        # File name to save the data to.
        self.db_file_name = db_file_name
        # The object that holds the actual data.
        self.data = Data(db_file_name)
        # List of menu items, their numbers, and methods.
        self.menu_items = [
            (self.QUIT, ' {}: {}'.format(self.QUIT, 'Quit'),
             None),
            (self.ADD, ' {}: {}'.format(self.ADD, 'Add an entry'),
             self.add),
            (self.EDIT, ' {}: {}'.format(self.EDIT, 'Edit an entry'),
             self.edit),
            (self.DEL, ' {}: {}'.format(self.DEL, 'Delete an entry'),
             self.delete),
            (self.SEARCH, ' {}: {}'.format(self.SEARCH, 'Search for an entry'),
             self.search),
            (self.LIST, ' {}: {}'.format(self.LIST, 'List all entries'),
             self.printAll),
            (self.SELECT, ' {}: {}'.format(self.SELECT, 'Select an entry'),
             self.select)]
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

    def selectOp(self):
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
            self.selectOp()

    def add(self):
        """
        Add entry.
        """
        # Get the name of the new entry.
        name = input('Input the name of the new entry: ')
        # Check if the key exists
        if self.data.isEntry(name):
            print('There is an existing entry under that name' +
                  ', you can only edit it.')
        else:
            # The key is OK, get the e-mail address.
            email = input('Input the e-mail address of the new entry: ')
            # Add the data.
            self.data.add(name, email)
            print('{} added'.format(name))
        # Be nice and select the entry.
        self.selected = name

    def edit(self):
        """
        Edit an entry.
        """
        # Check if a valid entry is selected.
        if self.selected is None:
            print('An entry must be selected')
        elif self.selected not in self.data.entries().keys():
            print('ERROR: Name "{}" not found'.format(self.selected))
            self.selected = None
        else:
            # Get new name.
            new_name = input(
                'Input the new name of the entry [{}]: '.format(self.selected))
            # Chose default on empty.
            if len(new_name) < 1:
                new_name = self.selected

            # Get new e-mail.
            email = input(
                'Input the new e-mail address of the entry [{}]: '.format(
                    self.data.entries()[self.selected]))
            # Chose default on empty.
            if len(email) < 1:
                email = self.data.entries()[self.selected]

            # Apply the changed data.
            self.data.edit(self.selected, new_name, email)
            # Select the item.
            self.selected = new_name
            print('{} changed'.format(self.selected))

    def delete(self):
        """
        Delete an entry.
        """
        # Check if a valid entry is selected.
        if self.selected is None:
            print('An entry must be selected')
        elif self.selected not in self.data.entries().keys():
            print('ERROR: Name "{}" not found'.format(self.selected))
            self.selected = None
        else:
            # Yep. Delete it.
            self.data.delete(self.selected)
            print('{} deleted'.format(self.selected))
            # Un-select.
            self.selected = None

    def search(self):
        """
        Search for an entry by a string.
        :return:
        """
        # Check if there are any entries.
        if self.data.n_entries():
            # Print some help.
            print('Supported search patterns:\n' +
                  ' *\tmatches everything\n' +
                  ' ?\t	matches any single character\n' +
                  ' [seq]\tmatches any character in seq\n' +
                  '[!seq]\tmatches any character not in seq\n')
            # Get the search string from the user.
            search_str = input('Input search string: ')
            # Search the data.
            self.data.search(search_str)

            # Print the number of entries found.
            if self.data.n_search_results() == 1:
                print('Found {} entry'.format(self.data.n_search_results()))
            else:
                print('Found {} entries'.format(self.data.n_search_results()))
            # Select item if it there is only one.
            if self.data.n_search_results() == 1:
                self.selected = self.data.search_results()[0]
            else:
                print('Use a more specific search string.')
        else:
            print('No entries')

    def select(self):
        """
        Select an entry.
        """
        # Are there any entries?
        if self.data.n_entries():
            # De-select currently selected.
            self.selected = None
            # Do a search.
            self.search()
            # If none is selected print the result of the search.
            if self.selected is None:
                self.printSearch()
        else:
            print('No entries')

    def printEntry(self, name, selection=True):
        """
        Print a named entry.

        :param name: The name of the entry.
        :param selection: Highlight selection.
        """
        # Check the key.
        if name not in self.data.entries().keys():
            print('ERROR: Name "{}" not found'.format(name))
        else:
            # Print and highlight selection.
            if selection and self.selected == name:
                print('* Name: {:20}'.format(name) + ' - ' +
                      'E-mail: {:>20} *'.format(self.data.email(name)))
            else:
                print('  Name: {:20}'.format(name) + ' - ' +
                      'E-mail: {:>20}'.format(self.data.email(name)))

    def printAll(self):
        """
        Print all entries.
        """
        if len(self.data.entries()) != 0:
            print('\nAll entries:')
            # Print all entries.
            for name in self.data.entries().keys():
                self.printEntry(name)
        else:
            # Tell that there are no entries.
            print('No entries')

    def printSearch(self):
        """
        Print all entries from the current search result.
        """
        # Result counter.
        i = 1

        # Print results.
        if self.data.n_search_results() == 0:
            print('No search results')
        else:
            for name in self.data.search_results():
                print(' {:d}; '.format(i), end='')
                self.printEntry(name)
                i += 1

    def save(self):
        """
        Save the data.
        """
        print('Saving data to ' + self.db_file_name)
        self.data.save()

    def load(self):
        """
        Load the data.
        """
        if self.data.load():
            print('Data loaded from ' + self.db_file_name)

    def run(self):
        """
        Load the data and enter the main loop. Save the data on exit.

        """
        # Load data.
        self.load()
        # No selection.
        self.data.selected = None

        # Let the user select an operation.
        self.selectOp()

        # Run until quit is selected.
        while self.op != 0:
            # Run the selected operation.
            self.menu_items[self.op][2]()
            # Let the user select an operation.
            self.selectOp()

        # Save the data.
        self.save()

        print('Bye.')
