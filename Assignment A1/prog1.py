#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: prog1
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (30/10-2016)
 
Program that prints some information about me.
'''

def main():
	# Print my name.
	print('Martin Bo Kristensen Grønholdt')
	# Print my address.
	print('Jacob Hansensvej 153, 1')
	# Print the zip code and city.
	print('5260 Odense S')
	# Tell that I was a "sproglig student" back in the days
	print('Language student')	

#Run this when invoked directly
if __name__ == '__main__':
	main()
