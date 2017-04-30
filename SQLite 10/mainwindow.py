# -*- coding: utf-8 -*-
"""
Name: GUI for customer database.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-26)

Main window.
"""

from PyQt5 import QtSql
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    """
    Class encapsulates the main window.
    """

    def __init__(self):
        """
        Constructor, creates the UI.
        """
        # Call the parent constructor.
        super().__init__()

        # Load the GUI definition from an XML file.
        uic.loadUi('mainwindow.ui', self)

        # Show window
        self.show()

    def error(self, msg):
        """
        Open a message box for errors.
        :param msg: The error message.
        """
        # Create an instance.
        mb = QMessageBox()
        # Set the window title.
        mb.setWindowTitle('Error')
        # Set the window content text
        mb.setText(msg)
        # Show the message box.
        mb.exec()

    def addClicked(self):
        """
        Handler that is called when the get config button is clicked
        """
        pass
