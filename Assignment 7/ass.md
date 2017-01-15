# Programming Exercises #
## Assignment 7 Lists and Tuples ##

This assignment will train Python: lists and Tuples, file handling, exception
handling, repetition structures: while and for loops, if-else, elif, input,
format, numbers, calculations.
In the text book “Starting Out with Python - 2nd Edition”, do chapter 8:
“Programming Exercises”:

 1. Total Sales
 2. Lottery Number Generator
 4. Number Analysis Program
 9. World Series Champions

The referenced files can be found on Fronter in a ZIP file.
On the next pages is shown output suggestions. These should be seen both as
inspiration or help and also as minimum requirements.

### Chapter 8 Exercise 1. Output suggestion. ###
    Enter sales for Monday   :    3545
    Enter sales for Tuesday  :    654
    Enter sales for Wednesday:    456
    Enter sales for Thursday :    54654
    Enter sales for Friday   :    654
    Enter sales for Saturday :    654
    Here are the sales you entered and the accumulated total:
    Monday    :    3545.00   Total:    3545.00
    Tuesday   :     654.00   Total:    4199.00
    Wednesday :     456.00   Total:    4655.00
    Thursday  :   54654.00   Total:   59309.00
    Friday    :     654.00   Total:   59963.00
    Saturday  :     654.00   Total:   60617.00
     
### Chapter 8 Exercise 2. Output suggestion. ###
    
    Next weeks winning lottery numbers are*:
        1     2     3     4     5     6     7
        0     9     6     8     8     3     7
    * maybe!


### Chapter 8 Exercise 9. Output suggestion. ###

Note that the list of winners is meant for debugging and should maybe be removed
from the production edition of the program. Further the input section is not 
very user friendly as the program just stops in case of the entry of a team not
in the winners list.

    Boston Americans            1
    New York Giants             5   
    Chicago White Sox           3
    Chicago Cubs                2
    Pittsburgh Pirates          5
    Philadelphia Athletics      5
    Boston Red Sox              6
    Boston Braves               1
    Cincinnati Reds             5
    Cleveland Indians           2
    New York Yankees           26
    Washington Senators         1
    St. Louis Cardinals        10
    Detroit Tigers              4
    Brooklyn Dodgers            1
    Milwaukee Braves            1
    Los Angeles Dodgers         5
    Baltimore Orioles           3
    New York Mets               2
    Oakland Athletics           4
    Philadelphia Phillies       2
    Kansas City Royals          1
    Minnesota Twins             2
    Toronto Blue Jays           2
    Atlanta Braves              1
    Florida Marlins             2
    Arizona Diamondbacks        1
    Anaheim Angels              1
    Type the team you are looking for: St. Louis Cardinals
    Team: St. Louis Cardinals has won: 10 times!

and
...

    Florida Marlins             2
    Arizona Diamondbacks        1
    Anaheim Angels              1
    Type the team you are looking for: Odense Boldklub
    Team Odense Boldklub was not found!

Challenge: Make the list either alphabetic or as shown here, numerically sorted:

    New York Yankees           26
    St. Louis Cardinals        10
    Boston Red Sox              6
    Los Angeles Dodgers         5
    Cincinnati Reds             5
    Philadelphia Athletic       5
    Pittsburgh Pirates          5
    New York Giants             5
    Oakland Athletics           4
    Detroit Tigers              4
    Baltimore Orioles           3
    Chicago White Sox           3
    Florida Marlins             2
    Toronto Blue Jays           2
    Minnesota Twins             2
    Philadelphia Phillies       2
    New York Mets               2
    Cleveland Indians           2
    Chicago Cubs                2
    Anaheim Angels              1
    Arizona Diamondbacks        1
    Atlanta Braves              1
    Kansas City Royals          1
    Milwaukee Braves            1
    Brooklyn Dodgers            1
    Washington Senators         1
    Boston Braves               1
    Boston Americans            1
    Type the team you are looking for: New York Giants
    Team: New York Giants has won: 5 times!


## 1. Total Sales ##

Design a program that asks the user to enter a store’s sales for each day of the
week. The amounts should be stored in a list. Use a loop to calculate the total
sales for the week and display the result.

## 2. Lottery Number Generator ##

Design a program that generates a seven-digit lottery number. The program should
generate seven random numbers, each in the range of 0 through 9, and assign each
number to a list element. (Random numbers were discussed in Chapter 6.) Then
write another loop that displays the contents of the list. 

## 4. Number Analysis Program ##

Design a program that asks the user to enter a series of 20 numbers. The program
should store the numbers in a list and then display the following data:

 * The lowest number in the list
 * The highest number in the list
 * The total of the numbers in the list
 * The average of the numbers in the list

## 9. World Series Champions ##

If you have downloaded the source code from this book’s companion Web site, you
will find a file named WorldSeriesWinners.txt in the Chapter 08 folder. This
file contains a chronological list of the World Series winning teams from 1903 
through 2009. (The first line in the file is the name of the team that won in
1903, and the last line is the name of the team that won in 2009. Note that the
World Series was not played in 1904 or 1994.) Write a program that lets the user
enter the name of a team and then displays the number of times that team has won
the World Series in the time period from 1903 through 2009. (You can access the
book’s companion Web site at www.pearsonhighered.com/gaddis.)
