#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: prog3
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (30/10-2016)
 
Program to convert square feet to acres.
'''
def main():
	# Get the area in square feet
	square_feet = input('Input the total square feet? ')
	# Calculate the acres, by first converting the input to
	# a floating point value, divide by 43560, convert this to a
	# string and add it to the initial message string.
	print('Acres: ' + str(float(square_feet) / 43560))

#Run this when invoked directly
if __name__ == '__main__':
	main()
