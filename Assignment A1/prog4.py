#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: prog4
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (30/10-2016)
 
Calculate the total price of a number of items, as well as the taxes
paid.
'''
def main():
	#Start with and emtpy total
	total_price = 0
	total_items = 0
	
	#Get the price
	price = input('Input item price (stop adding items by ' +
				  'inputting less than 1):')
	#Keep asking for the price of an item until the user inputs 0
	while price > 0:
		#Add the price of the new item
		total_price += float(price)
		#Keep count of the number of items added
		total_items += 1
		#Ask for the price of antoher item
		price = input('Input item price (stop adding items by ' +
				    'inputting less than 1):')

	#Print the subtotal
	print('\nThe subtotal price of your ' + str(total_items) +
		  ' items are: ' + str(float(total_price)))
	#Print the tax
	print('Sales tax (6%) amounts to: ' +
		  str(float(total_price) * 0.06))
	#Print the total price
	print('The total price for you items including tax is: ' +
		   str((total_price + float(total_price) * 0.06)))


#Run this when invoked directly
if __name__ == '__main__':
	main()
