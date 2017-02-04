#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 3 "Personal Information Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-04)

Program that uses a class to hold the personal information of a few people.
"""
import persinfo

def main():
    """
    Program main entry point.
    """
    # Create a list of people.
    people = list()
    # Populate 3 instances.
    people.append(
        persinfo.PersonalInfo('Martin B. K. Grønholdt', 'World', '500',
                              '123456789'))
    people.append(
        persinfo.PersonalInfo('Jonni Rabbit', 'Cage', '9+',
                              'none'))
    people.append(
        persinfo.PersonalInfo('Erling', 'Rat paradise', '3 (deceased)',
                              'none'))
    #Print all people.
    for person in people:
        print(person)


# Run this when invoked directly
if __name__ == '__main__':
    main()
