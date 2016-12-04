#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: prog5
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (30/10-2016)
 
Program to print the distance traveled at a speed of 60 mph in 5, 8,
and 12 hours.
'''
def main():
	#Speed in mph
	mph = 60
	
	#Print a message to tell what is calulated
	print('When traveling at ' + str(mph) + ' miles per hour:\n');
	
	#Loop through the values 5, 8, 12 which is the hours traveled.
	for hours in [5, 8, 12]:
		#Calculate and print the distance traveled by the formula
		#distance = hours * speed.
		print('The distance traveled after ' + str(hours) + ' is ' +
			   str(hours * mph) + ' miles.')
			   
#Run this when invoked directly
if __name__ == '__main__':
	main()
