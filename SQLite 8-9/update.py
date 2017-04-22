# -*- coding: utf-8 -*-
"""
Name: SQLite example of updating tables.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-04-22)
"""

# Import the SQLite module
import sqlite3


def printAllEntries():
    """
    Print all entries in the database.
    """
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


# Start an exception block to catch errors.
try:
    # Create a connection to a database with the file name 'example.db'. The
    # file is created if missing.
    conn = sqlite3.connect('example.db')

    # Get a Cursor object to used to perfom SQL commands on the database.
    cursor = conn.cursor()

    # Print all entries before changing them.
    printAllEntries()

    #Update the second and third fields address information.
    print('\nUpdating data in the database...', end='')
    # Yes we can have crummy chip references.
    cursor.execute('UPDATE customerTable SET address = ? WHERE idCust = ?',
                   ('Opampstreet 741', 2))

    cursor.execute('UPDATE customerTable SET address = ? WHERE idCust = ?',
                   ('Timerstreet 555', 3))
    # Commit the data to the database.
    conn.commit()
    print('done')

    # Print all entries again to show the changes.
    printAllEntries()


except sqlite3.Error as sql_error:
    print('\n\nAn database error occurred!')
    print('Error is: ' + str(sql_error))
