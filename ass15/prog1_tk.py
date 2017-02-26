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
import tkinter
from tkinter import StringVar


class MyGUI:
    def __init__(self, parent):
        """
        Constructor.
        Creates the UI components and layout.

        :param parent: The parant widget.
        """
        # Create the main window widget.
        self.parent = parent

        # Create a StringVar used to modify the label text.
        self.info_str = StringVar()

        # Create a Label widget
        self.info_label = tkinter.Label(self.parent,
                                        textvariable=self.info_str,
                                        height=3)
        # Place the label at the top of the grid layout
        self.info_label.grid(row=0, column=0, columnspan=3, padx=2, pady=2)

        # Create the buttons.
        self.info_button = tkinter.Button(self.parent,
                                          text='Show info',
                                          command=self.add_data)
        self.quit_button = tkinter.Button(self.parent,
                                          text='Quit',
                                          command=self.parent.destroy)

        # Add the buttons to the second row of the layout grid.
        self.info_button.grid(row=1, column=0, padx=5, pady=5)
        self.quit_button.grid(row=1, column=2, padx=5, pady=5)

    def add_data(self):
        """
        Event handler to add data to the label when the info button is pressed.
        """
        self.info_str.set('Steven Marcus\n' +
                          '274 Baily Drive\n' +
                          'Waynesville, NC 27999')


def main():
    """
    Main function, instantiates TK and the GUI class.
    """
    root = tkinter.Tk()
    # Create an instance of the MyGUI class.
    my_gui = MyGUI(root)
    # Enter the tkinter main loop
    tkinter.mainloop()


# Run this when invoked directly
if __name__ == '__main__':
    main()
