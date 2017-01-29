# -*- coding: utf-8 -*-
"""
Name: Program 8 "Name and Email Addresses"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-29)

Data handling code.
"""
import fnmatch
import pickle
import os.path


# noinspection PyPep8Naming
class Data:
    """
    This class does all data handling. It stores names and associated e-mail
    addresses.
    """

    def __init__(self, file_name):
        """
        Construct a data object for
        :param file_name: The name and path of the file used to store the data.
        """
        # The dictionary holding the data.
        self.data = dict()
        # Data file name
        self.file_name = file_name
        # List of last search results.
        self.data_search_results = list()

    def save(self):
        """
        Save the data using pickle. Complain and exit on error.
        """
        try:
            # Open the file for binary write access.
            with open(self.file_name, 'wb') as data_file:
                # Pickle the data to the file.
                pickle.dump(self.data, data_file)
        except IOError as ex:
            # Complain when something goes wrong with the file access.
            print('Exception: {}'.format(str(ex)))
            print('Error saving data.')
            exit(1)

    def load(self):
        """
        Load data from a file using pickle. Complain and exit on error.
        :return: True on success, False otherwise,
        """
        try:
            # Check if there is a file.
            if os.path.isfile(self.file_name):
                # Open the file.
                with open(self.file_name, 'rb') as data_file:
                    # Un-pickle the data
                    self.data = pickle.load(data_file)
                return True

            # Tell that load did not succeed, but the error was not fatal.
            return False
        except IOError as ex:
            # Complain when something goes wrong with the file access.
            print('Exception: {}'.format(str(ex)))
            print('Error saving data.')
            exit(1)

    def isEntry(self, name, error_not_found=False):
        """
        Check if name is in the data.

        :param name: The exact name to look for.
        :param error_not_found: Show an error if name is not found, is set to
                                True.
        :return: True if found, False otherwise.
        """
        # Default to not found.
        ret = False
        # Look for the key.
        if name in self.data.keys():
            ret = True
        else:
            # Print error if not found, and asked to.
            if error_not_found is True:
                print('ERROR: Name "{}" not found'.format(name))
        # Return result.
        return ret

    def n_entries(self):
        """
        Return the number of entries in the data.

        :return: Number of entries in the data.
        """
        return len(self.data)

    def entries(self):
        """
        Return a dictionary with all entries in the data.
        :return:
        """
        return self.data

    def add(self, name, email):
        """
        Add an entry to the data.

        :param name: Name to add.
        :param email:  E-mail to add.
        """
        # Check if the key is correct.
        if name is None:
            print('ERROR: Name can not be empty')
        elif len(name) < 1:
            print('ERROR: Name can not be empty')
        else:
            # Add/overwrite if it is.
            self.data[name] = email

    def edit(self, old_name, new_name, email):
        """
        Change an entry.

        :param old_name: The original name of the entry.
        :param new_name: the new name of the entry, None to keep the old.
        :param email: Email address to set for the entry.
        """
        # Keep the old name if no new is given
        if new_name is None:
            new_name = old_name

        # Add/Change the entry.
        self.add(new_name, email)

        # Delete the old entry if this is a new key.
        if old_name != new_name:
            self.delete(old_name)

    def delete(self, name):
        """
        Delete an entry.

        :param name: Name of the entry to delete.
        """
        # Check if the key is correct.
        if name is None:
            print('ERROR: Name can not be empty')
        elif len(name) < 1:
            print('ERROR: Name can not be empty')
        else:
            # Delete the entry if okay.
            del self.data[name]

    def email(self, name):
        """
        Return the e-mail address of an entry.

        :param name: Name of the entry.
        :return: E-mail address or empty string if not found.
        """
        # Default to empty string.
        email = ''

        # Do some validation.
        if name is None:
            print('ERROR: Name can not be empty')
        elif len(name) < 1:
            print('ERROR: Name can not be empty')
        elif len(self.data) < 1:
            print('ERROR: No entries')
        else:
            # The key checks out.
            email = self.data[name]
        # Return the e-mail address if found.
        return email

    def search(self, search_str):
        """
        Find a string in the data entries using fnmatch.

        :param search_str: String to search for including wildcards.
        :return: List of names that matches the search string.
        """
        # Use a set to keep the results so they only appear once.
        names = set()

        # Run through all entries.
        for name, email in self.data.items():
            # Search in both names and email addresses using fnmatch.
            if fnmatch.fnmatch(name, search_str):
                names.add(name)
            if fnmatch.fnmatch(email, search_str):
                names.add(name)

        # Convert the set to a list and return.
        self.data_search_results = list(names)

    def n_search_results(self):
        """
        Return the number of results of the last search.

        :return: Number of result of the last search.
        """
        return len(self.data_search_results)

    def search_results(self):
        """
        Return a list of names matching the last search.

        :return: List of names matching the last search.
        """
        return self.data_search_results
