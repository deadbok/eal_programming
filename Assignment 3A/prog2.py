#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
'''
Name: Program 2
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (19/11-2016)

Compare the area of two rectangles and tell which is the largest.
'''
def get_rectangle(name='no name'):
    '''
    Get the width an height of a rectangle from the user.

    :param name: Name of the rectangle that the values belong to.
    :return: Tuple (width, height)
    '''
    #Get width.
    print('Enter the width of rectangle {}: '.format(name), end='')
    width = float(input())
    #Get height.
    print('Enter the height of rectangle {}: '.format(name), end='')
    height = float(input())
    #Return the values as a tuple.
    return((width, height))


def get_rect_area(rect):
    '''
    Get the area of a rectangle.

    :param rect: Tuple (width, height) values for the rectangle.
    :return: Area of the rectangle.
    '''
    # Return the area.
    return(rect[0] * rect[1])

def print_rect(rect, name='no name'):
    '''
    Print the width, height, and area of a rectangle.

    :param rect: Tuple (width, height) values for the rectangle.
    '''
    print('Rectangle {}'.format(name) +
          ' has a width of {:0.2f}'. format(rect[0]) +
          ', a height of {:0.2f},'.format(rect[1]) +
          ' and an area of {}'.format(get_rect_area(rect)))


def main():
    '''
    Program main entry point.
    '''
    # The rectagnle sizes from the user.
    try:
        rect_a = get_rectangle('A')
        rect_b = get_rectangle('B')
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only numbers.')
        exit(1)

    # Print rectangle info.
    print()
    print_rect(rect_a, 'A')
    print_rect(rect_b, 'B')

    # Tell which rectangle has the largest area.
    if (get_rect_area(rect_a) > get_rect_area(rect_b)):
        print('Rectangle A has a larger area than rectangle B.')
    elif (get_rect_area(rect_a) < get_rect_area(rect_b)):
        print('Rectangle B has a larger area than rectangle A.')
    else:
        print('Rectangles A and B have equal areas.')


# Run this when invoked directly
if __name__ == '__main__':
    main()
