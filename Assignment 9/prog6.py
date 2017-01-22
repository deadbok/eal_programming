#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Program 4 "Average Number of Words"
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-01-22)

Read a file with one sentence per line, and calculates the average number of
words per sentence.
"""


def load_sentences(filename='textErrorList.txt'):
    """
    Load sentences from a file separated by lines.

    :return: List of sentences.
    """
    print('Loading text data...')
    # List of sentences
    sentences = list()
    # Load the file
    try:
        with open(filename, 'r') as data_file:
            for line in data_file:
                # Strip line endings
                sentences.append(line.strip())
    except IOError as ex:
        # Complain when something goes wrong with the file access.
        print('Exception: {}'.format(str(ex)))
        print('Error loading text.')
        exit(1)
    print('OK\n')
    return (sentences)


def count_words(sentences):
    """
    Count words in a list of sentences separated by space.

    :param sentences: List of sentences.
    :return: Number of words.
    """
    # Count all words and print what is going on.
    i = 1
    total_n_words = 0
    for sentence in sentences:
        # Split word by spaces
        words = sentence.split()
        n_words = len(words)
        total_n_words += n_words
        print('Line {:2}, {:2} words:\t{}'.format(i, n_words,
                                                  str(words).strip("[]")))
        i += 1
    return (total_n_words)


def main():
    """
    Program main entry point.
    """
    sentences = load_sentences()
    n_words = count_words(sentences)
    # Print result.
    print('\nAverage number of words per sentence: {:.2f}'.format(
        n_words / len(sentences)))


# Run this when invoked directly
if __name__ == '__main__':
    main()
