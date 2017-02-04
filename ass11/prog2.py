#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 2 "Car Class"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-02-01)

Program that drives a car.
"""
import car


def main():
    """
    Program main entry point.
    """
    # Instantiate the car class.
    my_car = car.Car(1989)

    # Print the static car data.
    print('The car:\n{}'.format(my_car))

    # Print the initital speed.
    print('Current speed: {}'.format(my_car.get_speed()))

    # Accelerate 5 times and print the speed.
    for counter in range(5):
        my_car.accelerate()
        print('Current speed: {}'.format(my_car.get_speed()))

    # De-accelerate 5 times and print the speed.
    for counter in range(5):
        my_car.brake()
        print('Current speed: {}'.format(my_car.get_speed()))


# Run this when invoked directly
if __name__ == '__main__':
    main()
