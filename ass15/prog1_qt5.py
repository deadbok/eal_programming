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

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, \
    QLabel


class Prog1UI(QWidget):
    """
    Class that creates a simple dialog window.
    """

    def __init__(self):
        """
        Constructor, creates the UI.
        """
        # Call the parant constructor.
        super().__init__()

        # Create the label, using a member variable to be able to reference it
        # later.
        self.address_label = QLabel('\n\n')

        # Create the buttons
        info_button = QPushButton("Show info")
        quit_button = QPushButton("Quit")

        # Create a grid layout
        grid = QGridLayout()
        grid.setSpacing(10)

        # Place the address labe in the top row of the grid and make it span 5
        # columns.
        grid.addWidget(self.address_label, 0, 0, 1, 5)

        # Place the buttons at the second row, with some cells between them for
        # spacing.
        grid.addWidget(info_button, 1, 1)
        grid.addWidget(quit_button, 1, 3)

        # Connect event handler for button clicks
        info_button.clicked.connect(self.infoClicked)
        # Close the window on clicking "Quit"
        quit_button.clicked.connect(self.close)

        # Set the layout of this widget
        self.setLayout(grid)

        # Set title
        self.setWindowTitle('Program 1 QT5 GUI')
        # Show window
        self.show()

    def infoClicked(self):
        """
        Handler that is called when the info button is clicked
        """
        # Set the text of the label
        self.address_label.setText('Steven Marcus\n' +
                                   '274 Baily Drive\n' +
                                   'Waynesville, NC 27999')


def main():
    """
    Main program
    """
    # Instantiate the QT application class
    app = QApplication(sys.argv)
    # Create out window
    ui = Prog1UI()
    # Exit when done.
    sys.exit(app.exec_())


# Run this when invoked directly
if __name__ == '__main__':
    main()
