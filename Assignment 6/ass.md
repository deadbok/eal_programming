# Programming Exercises #
## Assignment 6 ##

This assignment will train Python: file handling, exception handling, repetition structures: while
and for loops, if-else, elif, input, format, numbers, calculations.
Caution: When using the “open” function to operate on files with the ‘w’ option, you erase files
content. Double check what files you operate on and what option is chosen to avoid accidentally
erasing a file.
In the text book “Starting Out with Python - 2nd Edition”, do chapter 7: “Programming Exercises”:

 1. File Display. Make the program both append to the actual file and to show the
    content. See output suggestion hereafter.
 2. File Head Display
 6. Average of Numbers
 7. Random Number File Writer
 8. Random Number File Reader
 9. Exception Handing
Challenge:
 10. Golf Scores

Remember to read and comply with the “Hand in requirements” listed first in this document.

## File Display ##

Assume that a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that displays all of the numbers in the file.
Programming Exercises

###Chapter 7 Exercise 1. Output suggestion.###

    This program prompts the user for a series of numbers
    and stores them in a file named numbers.txt
    End the entry by typing: "0"
    Enter number: 4
    Enter number: 5
    Enter number: 6
    Enter number: 0
    Data written to numbers.txt.
    Now listing the content of the file numbers.txt
    4.00
    5.00
    6.00
    -------------------
    End of file reached

## File Head Display ##

Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should dis-
play the file’s entire contents.

###Chapter 7 Exercise 2. Output suggestion.###

    Display file header.
    Enter name of file to be displayed: testText.txt
    ------------------
    Line 1: This is a test
    Line 2: text to test a
    Line 3: Python program.
    Line 4: Only 4 lines long.
    End of file reached

## Average of Numbers ##

Assume that a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in
the file.


## Random Number File Writer ##

Write a program that writes a series of random numbers to a file. Each random number
should be in the range of 1 through 100. The application should let the user specify how
many random numbers the file will hold.

###Chapter 7 Exercise 6. Output suggestion.###

    Program writes random numbers to file random.txt
    Enter number of numbers to be generated: 5
    ----------------------------
    Line 1: 46.00
    Line 2: 50.00
    Line 3: 18.00
    Line 4: 76.00
    Line 5: 51.00
    ----------------------------
    The number of numbers is: 5

## Random Number File Reader ##

This exercise assumes you have completed Programming Exercise 7, Random Number File
Writer. Write another program that reads the random numbers from the file, display the
numbers, and then display the following data:

 * The total of the numbers
 *  The number of random numbers read from the file

## Exception Handing ##

Modify the program that you wrote for Exercise 6 so it handles the following exceptions:

 * It should handle any IOError exceptions that are raised when the file is opened and data
   is read from it. 
 * It should handle any ValueError exceptions that are raised when the items that are read
   from the file are converted to a number.
   
###Chapter 7 Exercise 9. Output suggestion.###

    Program sums numbers in a file.
    Enter name of file to be summed: random.txt
    -------------------------------------------
    Line 1:
     3.00:
     3.00
    Line 2: 61.00: 64.00
    Line 3: 26.00: 90.00
    Line 4: 98.00: 188.00
    File random.txt possibly contains wrong data. E.g. non numeric values.
    Program terminated.
    could not convert string to float: 'hello\n'
    
Here a file that does not exist is entered:

    Program sums numbers in a file.
    Enter name of file to be summed: ramdom.txt
    ------------------
    File ramdom.txt does not exist.
    Enter name of file to be summed: random.txt
    ------------------
    Line 1:
     3.00:
     3.00
    Line 2: 61.00: 64.00
    Line 3: 26.00: 90.00
    Line 4: 98.00: 188.00
    File random.txt possibly contains wrong data. E.g. non numeric values.
    Program terminated.
    could not convert string to float: 'hello\n'

## Golf Scores ##

The Springfork Amateur Golf Club has a tournament every weekend. The club president
has asked you to write two programs:
 1 A program that will read each player’s name and golf score as keyboard input, and then
    save these as records in a file named golf.txt. (Each record will have a field for the
    player’s name and a field for the player’s score.)
 2 A program that reads the records from the golf.txt file and displays them.
