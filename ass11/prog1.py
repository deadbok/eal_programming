#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 1 "Pet Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-01)

Program to organise name and email addresses.
"""
import pet

def main():
    """
    Program main entry point.
    """
    # Instantiate the application class.
    my_pet = pet.Pet()

    try:
        my_pet.set_name(input('Input the name of the pet: '))
        my_pet.set_animal_type(input('Input the type of the pet: '))
        my_pet.set_age(int(input('Input the age of the pet: ')))
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nThe input was wrong.')
        exit(1)

    print(my_pet)



# Run this when invoked directly
if __name__ == '__main__':
    main()
