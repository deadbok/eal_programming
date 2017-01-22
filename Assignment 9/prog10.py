#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 9 "Most Frequent Character"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-22)

Display the most frequent character in a string entered by the user.
"""


def ch_freqency(data):
    """
    Count the occurrence of each character in the data, and return the count in
    a dictionary.

    :param data: Input string
    :return: List of tuples (character, count).
    """
    # Dictionary to keep count
    counts = dict()
    # Strip whitespaces and lowercase.
    data = ''.join(data.split()).lower()
    # Run through all characters.
    for ch in data:
        # Create a new entry if it is not there, else add.
        if ch not in counts.keys():
            counts[ch] = 1
        else:
            counts[ch] += 1

    # The final list.
    ret = list()
    # Sort the dictionary entries by value, and them to a list as tuples.
    for w in sorted(counts, key=counts.get, reverse=True):
        ret.append((w, counts[w]))

    return ret


def main():
    '''
    Program main entry point.
    '''
    # Get string from user.
    user_str = input('Input a string: ')

    # Count the characters
    counts = ch_freqency(user_str)

    # Get the highest count from the sorted list.
    max = counts[0][1]
    # List of other characters with max count.
    other_ch = list()
    # Just a counter.
    i = 1
    # Current entry
    count = counts[i]
    # Find all other characters that occur as many times as the most occurring.
    while count[1] == max:
        other_ch.append(count[0])
        i += 1
        count = counts[i]

    # Print the result.
    print('Most frequent character "{}" occurs {} times'.format(counts[0][0],
                                                                counts[0][1]),
          end='')

    # Print contenders or end the line.
    if len(other_ch):
        print(' (characters that occur the same number of times: {}).'.format(
            str(other_ch).strip("[]")))
    else:
        print('.')


# Run this when invoked directly
if __name__ == '__main__':
    main()
