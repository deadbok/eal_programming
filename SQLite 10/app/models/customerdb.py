import sqlite3
from flask import g
from flask import current_app

DATABASE = 'customers.db'


class CustomerDB:
    tableName = 'customerTable'

    def __init__(self):
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
        
        :return: 
        """
        # Get an active connection to the database if there is one.
        db = getattr(g, '_database', None)
        # Create a new one of no connection was available.
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)

        db.row_factory = sqlite3.Row

        return db

    def add(self, name='', email='', address='', city=''):
        """
        Add a customer to the table.
        :param name: 
        :param email: 
        :param address: 
        :param city: 
        :return: 
        """
        self.query_db(
            'INSERT INTO {}(name, email, address, city) VALUES(?,?,?,?)'.format(
                self.tableName), [name, email, address, city])

    def getAll(self):
        print(str(self.query_db('SELECT * FROM ' + self.tableName)))
        return self.query_db('SELECT * FROM ' + self.tableName)

    def query_db(self, query, args=(), one=False):
        """
        Helper function to do a query on the database.
        
        :param query: 
        :param args: 
        :param one: 
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

        # If there is stuff in the table
        if values:
            if one:
                # Return the first if thats what we were asked
                ret = values[0]
            else:
                # Return all results
                ret = values

        # Return the result
        return ret
