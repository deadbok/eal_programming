# -*- coding: utf-8 -*-
"""
Name: Database abastraction code.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0.0 (2017-04-30)
"""
import sqlite3
from flask import g
from flask import current_app

DATABASE = 'customers.db'


class CustomerDB:
    tableName = 'customerTable'

    def __init__(self):
        """
        Contrusctor that creates the database table if not there.
        """
        # Get the current tables in the database.
        db = self.__get_db()
        tables = db.execute(
            "SELECT name FROM sqlite_master WHERE type='table';")
        # Variable to indicate if the customerTable table exists
        created = False
        # Run through all table names.
        for table in tables:
            # If customerTable exists, do tell.
            if table[0] == self.tableName:
                created = True
        # Create the customerTable, if it is not there
        if not created:
            current_app.logger.debug("Creating table.")
            db.execute(
                """
                CREATE TABLE {} (
                  idCust INTEGER PRIMARY KEY,
                  name VARCHAR(100),
                  email VARCHAR(50),
                  address VARCHAR(50),
                  city VARCHAR(30)
                )""".format(self.tableName)
            )
            db.commit()

    def __get_db(self):
        """
        Get a connection to the database.
        
        :return: Database connection. 
        """
        # Get an active connection to the database if there is one.
        db = getattr(g, '_database', None)
        # Create a new one of no connection was available.
        if db is None:
            db = g._database = sqlite3.connect(current_app.config['DATABASE'])

        db.row_factory = sqlite3.Row

        return db

    def add(self, name='', email='', address='', city=''):
        """
        Add a customer to the table
        
        :param name: Customer name.
        :param email: Customer email.
        :param address: Customer address.
        :param city: Customer city.
        :return: 
        """
        # Do the query to insert the data.
        self.query_db(
            'INSERT INTO {}(name, email, address, city) VALUES(?,?,?,?)'.format(
                self.tableName), [name, email, address, city])

    def getAll(self):
        """
        Get all customer entries.
        """
        return self.query_db('SELECT * FROM ' + self.tableName)

    def query_db(self, query, args=(), one=False):
        """
        Helper function to do a query on the database.
        
        :param query: The SQL command.
        :param args: The arguments to the SQL.
        :param one: Set to true to return only the fist result.
        :return: 
        """
        # Default is to empty list.
        ret = []
        # Execute the query.
        db = self.__get_db()
        cur = db.execute(query, args)
        db.commit()
        # Get all data.
        values = cur.fetchall()
        # Close connection
        cur.close()

        # If there is stuff in the result.
        if values:
            if one:
                # Return the first if thats what we were asked
                ret = values[0]
            else:
                # Return all results
                ret = values

        # Return the result
        return ret
