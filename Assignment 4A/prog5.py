#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 5
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (13/11-2016)

Get the name of a secondary colour created from mixing to primary colours.
"""


def get_color():
    """
    Get the name of a primare color from the user.

    :return: 'red', 'blue', or 'yellow'.
    """
    # Get the colour from the user, convert to lower case.
    color = input('Enter the name of a primary colour: ').lower()
    # Raise an exception if the input is invalid.
    if color not in ['red', 'blue', 'yellow']:
        raise ValueError
    # Return the color.
    return (color)


def mix_colors(first_color, second_color):
    """
    Return the secondary colour resulting from mixing two primare ones.

    :param first_color: The first primary colour.
    :param second_color: The second primary colour.
    :return: The resulting secondary colour.
    """
    # Create a look up table for all colour mixes.
    color_look_up = {'red':
                         {'red': 'red',
                          'blue': 'purple',
                          'yellow': 'orange'},
                     'blue':
                         {'red': 'purple',
                          'blue': 'blue',
                          'yellow': 'green'},
                     'yellow':
                         {'red': 'orange',
                          'blue': 'green',
                          'yellow': 'yellow'}
                     }
    # Return the secondary colour.
    return (color_look_up[first_color][second_color])


def main():
    """
    Program main entry point.
    """
    # Get the colours from the user.
    try:
        first_color = get_color()
        second_color = get_color()
    except ValueError:
        # Complain when something unexpected was entered.
        print('\nPlease use only "red", "blue", and "yellow".')
        exit(1)

    # Print the result
    print('\nMixing the primary colours ' + first_color + ' and ' +
          second_color + ' results in the secondary colour ' +
          mix_colors(first_color, second_color))


# Run this when invoked directly
if __name__ == '__main__':
    main()
