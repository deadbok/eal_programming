#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Junpier configuration snatcher
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-07)

Program to download the configuration from a Junpier device.
"""

import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, \
    QLabel, QLineEdit, QPlainTextEdit

from vsrx import VSRX


class MainWindow(QWidget):
    """
    Class encapsulates the main window.
    """

    def __init__(self):
        """
        Constructor, creates the UI.
        """
        # Call the parent constructor.
        super().__init__()

        # Create the labels.
        ip_label = QLabel('Juniper IP address:')
        file_name_label = QLabel('Configuration file name:')
        config_label = QLabel('Configuration:')

        #Create the IP and file name edits.
        self.ip_edit = QLineEdit()
        #self.ip_edit.setInputMask('000.000.000.000')
        self.ip_edit.setPlaceholderText('127.0.0.1')
        self.file_name_edit = QLineEdit()

        #Create the configuration file view.
        self.config_edit = QPlainTextEdit()

        # Create the buttons
        get_button = QPushButton("Get configuration")
        # Connect the get config button to the handler.
        get_button.clicked.connect(self.getConfigClicked)

        quit_button = QPushButton("Quit")
        # Close the window on clicking "Quit"
        quit_button.clicked.connect(self.close)

        # Create a grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        # Place the labels in the top row.
        grid.addWidget(ip_label, 0, 0, 1, 1)
        grid.addWidget(file_name_label, 0, 2, 1, 1)

        # Place the edit fields on the next line.
        grid.addWidget(self.ip_edit, 1, 0, 1, 2)
        grid.addWidget(self.file_name_edit, 1, 2, 1, 4)

        #Place the configuration view label on the next line.
        grid.addWidget(config_label, 2, 0)

        # Place the configuration view.
        grid.addWidget(self.config_edit, 3, 0, 1, 6)

        # Place the buttons at the second row, with some cells between them for
        # spacing.
        grid.addWidget(get_button, 4, 3)
        grid.addWidget(quit_button, 4, 5)

        # Set the layout of this widget
        self.setLayout(grid)

        # Set title
        self.setWindowTitle('Juniper configuration snatcher')
        # Show window
        self.show()

        self.vsrx = VSRX()

    def getConfigClicked(self):
        """
        Handler that is called when the get config button is clicked
        """
        ip = self.ip_edit.text()
        if ip == '':
            ip = '127.0.0.1'
        self.vsrx.connect(ip,port=22222)
        config = self.vsrx.showConfiguration()
        self.config_edit.setPlainText(config)
