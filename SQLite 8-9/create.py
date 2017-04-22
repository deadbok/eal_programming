# -*- coding: utf-8 -*-
"""
Name: SQLite example of creating tables and inserting rows.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-04-22)
"""

# Import the SQLite module
import sqlite3

# Start an exception block to catch errors.
try:
    # Create a connection to a database with the file name 'example.db'. The file
    # is created if missing.
    conn = sqlite3.connect('example.db')

    # Get a Cursor object to used to perfom SQL commands on the database.
    cursor = conn.cursor()

    # Create the customerTable table.
    print('Creating customerTable...', end='')
    cursor.execute(
        """
        CREATE TABLE customerTable(
          idCust INT NOT NULL UNIQUE,
          name VARCHAR(100),
          email VARCHAR(50),
          address VARCHAR(50),
          city VARCHAR(30),
          PRIMARY KEY (idCust)
        )
        """
    )

    # Insert the data in to the table.
    cursor.execute(
        """
        INSERT INTO customerTable VALUES(
        1,
        'Per',
        'pda@eal.dk',
        'Mystreet1',
        'Odense'
        )
        """
    )
    # Can we make the street name Opampstreet to fit the number? ;-)
    cursor.execute(
        """
        INSERT INTO customerTable VALUES(
        2,
        'Artur',
        'at@hotmail.com',
        'Allstreet 741',
        'Vilnius'
        )
        """
    )
    cursor.execute(
        """
        INSERT INTO customerTable VALUES(
        3,
        'Alice',
        'ab@gmail.com',
        'Topstreet 56',
        'London'
        )
        """
    )
    # Commit the data to the database.
    conn.commit()
    print('done')

    print('\nCurrent entries in the database:')
    # Select all rows in the customerTable table.
    cursor.execute('SELECT * FROM customerTable')
    # A counter to make things look nice in the output.
    row_nr = 0
    # Run trhough all rows.
    for row in cursor.fetchall():
        # Next row number.
        row_nr += 1
        # Print row number.
        print('Row {}: '.format(row_nr), end='')
        # Run through all fields in the row.
        for field in row:
            # Print the fields.
            print('{}, '.format(field), end='')
        # Next line.
        print()

except sqlite3.Error as sql_error:
    print('\n\nAn database error occurred!')
    print('Error is: ' + str(sql_error))
