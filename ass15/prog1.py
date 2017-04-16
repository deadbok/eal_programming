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
        # Create the main window widget.
        self.parent = parent

        self.info_str = StringVar()


        # Create a Label widget containing
        self.info_label = tkinter.Label(self.parent, textvariable=self.info_str, font="-size 18", height=3)
        # Call the Label widget's pack method.
        self.info_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.info_button = tkinter.Button(self.parent, text='Show info', command=self.do_something, font="-size 18")
        self.quit_button = tkinter.Button(self.parent, text='Quit', command=self.parent.destroy, font="-size 18")

        self.info_button.grid(row=1, column=0, padx=5, pady=5)
        self.quit_button.grid(row=1, column=2, padx=5, pady=5)
        self.info_str.set(' ' * 38 + '\n\n')


    def do_something(self):
        self.info_str.set('Steven Marcus\n274 Baily Drive\nWaynesville, NC 27999')

def main():
    root = tkinter.Tk()
    root.minsize(width=450, height=240)
    # Create an instance of the MyGUI class.
    my_gui = MyGUI(root)
    # Enter the tkinter main loop
    tkinter.mainloop()

# Run this when invoked directly
if __name__ == '__main__':
    main()
