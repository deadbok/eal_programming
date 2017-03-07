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

import sys

from PyQt5.QtWidgets import QApplication
from ass33 import mainwindow


def main():
    """
    Main program
    """
    # Instantiate the QT application class
    app = QApplication(sys.argv)
    # Create out window
    ui = mainwindow.MainWindow()
    # Exit when done.
    sys.exit(app.exec_())


# Run this when invoked directly
if __name__ == '__main__':
    main()
