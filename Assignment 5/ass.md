# Programming Exercises #
## Assignment 5 Value returning functions ##

This assignment will train Python: value returning functions, repetition
structures: while and for loops, if-else, elif, input, format, numbers,
calculations.

1. In the text book “Starting Out with Python - 2nd Edition”, do chapter 6:
   “Programming Exercises”:
    1. Feet to Inches
    2. Math Quiz
    6. Test Average and Grade
    12. Rock, Paper, Scissors Game. See next page for output suggestion.
        * Draw a UML Activity Diagram for Exercise 12.
        * Draw the Hierarchy Diagram for Exercise 12.
2. Challenge:
    11. Random Number Guessing Game. See next page for output suggestion.
       Remember to read and comply with the “Hand in requirements” listed first
       in this document.
       
## 1. Feet to Inches ##

One foot equals 12 inches. Write a function named feet_to_inches that accepts a
number of feet as an argument, and returns the number of inches in that many
feet. Use the function in a program that prompts the user to enter a number of
feet and then displays the number of inches in that many feet.

## 2. Math Quiz ##

Write a program that gives simple math quizzes. The program should display two
random numbers that are to be added, such as:

      247
    + 129
    
The program should allow the student to enter the answer. If the answer is
correct, a message of congratulations should be displayed. If the answer is
incorrect, a message showing the correct answer should be displayed.

## 6. Test Average and Grade ##

Write a program that asks the user to enter five test scores. The program should
display a letter grade for each score and the average test score. Write the
following functions in the program:

 * `calc_average`: This function should accept five test scores as arguments and
   return the average of the scores.
 * `determine_grade`: This function should accept a test score as an argument and
   return a letter grade for the score, based on the following grading scale:


 Score    | Letter Grade
----------|---------------
 90–100   | A
 80–89    | B
 70–79    | C
 60–69    | D
 Below 60 | F

## 12. Rock, Paper, Scissors Game ##

Write a program that lets the user play the game of Rock, Paper, Scissors
against the computer. The program should work as follows.

1. When the program begins, a random number in the range of 1 through 3 is
   generated.

    * If the number is 1, then the computer has chosen rock.
    * If the number is 2, then the computer has chosen paper.
    * If the number is 3, then the computer has chosen scissors.

    (Don’t display the computer’s choice yet.)

2. The user enters his or her choice of “rock”, “paper”, or “scissors” at the
   keyboard.

3. The computer’s choice is displayed.

4. A winner is selected according to the following rules:
    * If one player chooses rock and the other player chooses scissors, then
      rock wins. (The rock smashes the scissors.)
    * If one player chooses scissors and the other player chooses paper, then
      scissors wins. (Scissors cuts paper.)
    * If one player chooses paper and the other player chooses rock, then paper
      wins. (Paper wraps rock.)
    * If both players make the same choice, the game must be played again to
      determine the winner.

## 11. Random Number Guessing Game ##

Write a program that generates a random number in the range of 1 through 100 and
asks the user to guess what the number is. If the user’s guess is higher than
the random number, the program should display "Too high, try again." If the
user’s guess is lower than the random number, the program should display "Too
low, try again." If the user guesses the number, the application should
congratulate the user and then generate a new random number so the game can
start over.

**Optional Enhancement:** Enhance the game so it keeps count of the number of
guesses that the user makes. When the user correctly guesses the random number,
the program should display the number of guesses.
