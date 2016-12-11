#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2016-12-04)

Print a christmas tree.

                   *
                  ***
                 *VO*V
                *****i*
               ****iiV*O
              V***O*OO***
             **OO********O
            *V*******VVO***
           **OV*******V*O*i*
          *OV*****Vi**V***O**
         iii*V******VO******i*
        **V****i*ii***i******iO
                  ***
                  ***

        Balls: 15 Pct:  10.42
        Cones: 15 Pct:  10.42
        Candl: 14 Pct:   9.72
        Stars: 100 Pct: 69.44
        ----------------------
        Total: 144 Pct: 100.00
"""

class ChristmasTree:
    
def tingel_tangel(distrubution=(10, 10, 10, 70)):


def tree(width, height):
    '''
    Print the tree.

    :param width:
    :return:
    '''
    # Find the middle of the tree.
    tree_middle = int(width / 2)
    # Row width of the top.
    row_width = 1
    # Loop from the top down.
    for h in range(0, height):
        # Loop from left to right.
        for w in range(0, width):
            # Print the filling spaces beofre the tree.
            if w < (tree_middle - int(row_width / 2)):
                print(' ', end='')
            # Print the rows of the tree itself.
            elif w <= (tree_middle + int(row_width / 2)):
                print('*', end='')
            # Print the top.
            elif row_width == 1 and w == tree_middle:
                print('*', end='')
        # New line.
        print()
        # Next row is wider.
        row_width += 2


def stem(tree_width, stem_width):
    '''
    Print the stem of the christmas tree.

    :param tree_width: Width of the christmas tree.
    :param stem_width: Width of the christmas tree stem.
    :return: Nothing.
    '''
    #Find the offset where the stem starts
    stem_start = int(tree_width / 2 - 1)
    for h in range(0, 2):
        # Loop until the
        for w in range(0, stem_start + stem_width):
            if w < stem_start:
                print(' ', end='')
            else:
                print('*', end='')
        print()


def main():
    '''
    Program main entry point.
    '''
    # Set percentage for the decorations.
    balls = 10
    candles = 10
    cones = 10
    stars = 70

    # Size of the tree, keep thw width an uneven number.
    width = 23
    height = 12
    stem_width = 3

    tree(width, height)
    stem(width, stem_width)




# Run this when invoked directly
if __name__ == '__main__':
    main()
