#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Customer database
Author: Martin Bo Kristensen Grønholdt
Version: 1.0 (2017-04-26)

Program to store customer information in a database.
"""

import sys

from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow


def main():
    """
    Main program
    """
    # Instantiate the QT application class
    app = QApplication(sys.argv)
    # Create out window
    ui = MainWindow()
    # Exit when done.
    sys.exit(app.exec_())


# Run this when invoked directly
if __name__ == '__main__':
    main()
