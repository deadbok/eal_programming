#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program  5 "RetailItem Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-19)

Program for entering details in to a ProductionWorker class.
"""
from ass12.retailitem import RetailItem


def main():
    """
    Program main entry point.
    """
    items = list()
    # Create 3 RetialItems in the list.
    items.append(RetailItem('Jacket', 12, 59.95))
    items.append(RetailItem('Designer Jeans', 40, 34.95))
    items.append(RetailItem('Shirt', 20, 24.95))

    # Print the items in a table, first the header.
    print('\n-----------------------------------------------------------' +
          '-----------')
    print('| #         | Description          | Units in inventory |' +
          ' Price      |')
    print('-----------------------------------------------------------' +
          '-----------')
    # Print the items.
    for i in range(len(items)):
        item = items[i]
        print('| Item {:4} | {:>20} |'.format(i + 1, item.get_description()),
              end='')
        print(' {:18.0f} | {:10.2f} |'.format(item.get_inventory(),
                                              item.get_price()))
    # Close the table.
    print('------------------------------------------------------------' +
          '----------')


# Run this when invoked directly
if __name__ == '__main__':
    main()
