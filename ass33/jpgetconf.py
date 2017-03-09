#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Junpier configuration snatcher
Author: Martin Bo Kristensen Grønholdt, Rickie Ljungberg, Kasper Soelberg.
Version: 1.0 (2017-03-09)

Program with a nice GUI to get the configuration from a Juniper device.
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
