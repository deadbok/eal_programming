#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: prog2
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (30/10-2016)
 
Program to print the projected profit of a sale.
'''
def main():
	# Get the total sales from via user input.
	total_sale = input('What is the projected total sale? ')
	# Calculate the total profit, by first converting the input to
	# an floating point value, then calculate the 23%, convert this to a
	# string and add it to the initial message string.
	print('Projected profit (23%): ' + str(0.23 * float(total_sale)))

#Run this when invoked directly
if __name__ == '__main__':
	main()
