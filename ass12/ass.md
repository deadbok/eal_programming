# Programming Exercises #
## Assignment 12 Classes and objects ##

This assignment will train Python: classes, objects - instances, dictionary,
pickling and subjects from the previous chapters.

In the text book "Starting Out with Python - 2nd Edition", do chapter 11: 
"Programming Exercises":

 **5**, **7** and **8** and

**9**: It is compulsory to use questions from the books Review Questions
sections. Copy paste the questions and multiple choices into a text file and
load the questions and answers from the file into objects. See file example
below.

**10**: Draw the UML graphic representation/ diagram for each of the involved
classes in exercise 8.

**11**: Draw a Hierarchy diagram for exercise 8. See the figure below from
program: auto_repair_payroll.py, for inspiration

 *Image not included*
    
Write exactly 9 lines of explanation to the hierarchy diagram.

**Challenge**:

 * Make the program randomly choose questions from the/more question and answers
   files.
 * Make the program list the questions and wrong and correct answers. This is
   seen in the output suggestion below.

The figure below shows a file where the multiple choice questions and answers
and the correct answer number are listed in the order:

 1. Question
 2. Answer option 1
 3. Answer option 2
 4. Answer option 3
 5. Answer option 4
 6. Correct answer number.
 
Note that the file has been graphically cropped, but it should still be able to
illustrate the idea. The file name is triviaQuestionsChap11.txt and it can be
found on Fronter.

 *Image of the contents of a text file!!! Not included*
 
**Chapter 11 Exercise 7. Output suggestion.**

Below is shown an output suggestion. Of course a real world program would clear
the screen and not print the screens/menues in a long sequence. But here this is
done to show the purchase sequence.
There is left room for improvement. E.g. should the program stay in the Purchase
menu and display the possible items until the user chooses to exit. The shown
"units" number is irrelevant in this program.

    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 1
    -----------------------------------
    Enter the number you want to purchase:
    1 : Jacket
    2 : Pullover
    3 : Trousers
    Enter a valid choice: 1
    *** Description     Jacket
    Units               12
    Price               151.95
    
    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 1
    -----------------------------------
    Enter the number you want to purchase:
    1 : Jacket
    2 : Pullover
    3 : Trousers
    Enter a valid choice: 2
    *** Description     Pullover
    Units               13
    Price               52.95
    
    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 1
    -----------------------------------
    Enter the number you want to purchase:
    1 : Jacket
    2 : Pullover
    3 : Trousers
    Enter a valid choice: 3
    *** Description     Trousers
    Units               14
    Price               85.95
    
    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 3
    Description         Jacket
    Units               12
    Price               151.95
    
    Description         Pullover
    Units               13
    Price               52.95
                     
    
    Description         Trousers
    Units               14
    Price               85.95
    
    ----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 2
    total:   151.95
    total:   204.90
    total:   290.85
    
    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 4
    Emptying cash register
    
    -----------------------------------
    Menu
    -----------------------------------
    1. Select items to buy
    2. Get total in cash register
    3. Show bought items
    4. Clear cash register
    5. Quit the program
    -----------------------------------
    Enter your choice: 5
    Good buy
    
**Chapter 11 Exercise 8. Output suggestion.**

    --------------------------------------------------
    Player 1 question: 1
    --------------------------------------------------
    The ______________ programming practice is centred on creating functions that are separate from the data that they work
    on.
    Enter the number for the correct answer: To exit enter "0"
    1: modular
    2: procedural
    3: functional
    4: object-oriented
    Your answer:2
    --------------------------------------------------
    Player 1 question: 2
    --------------------------------------------------
    The ______________ programming practice is centred on creating objects.
    Enter the number for the correct answer: To exit enter "0"
    1: object-centric
    2: objective
    3: procedural
    4: object-oriented
    Your answer:4
    --------------------------------------------------
    Player 1 question: 3
    --------------------------------------------------
    A(n) ______________ is a component of a class that references data.
    Enter the number for the correct answer: To exit enter "0"
    1: method
    2: instance
    3: data attribute
    4: module
    Your answer:1
    --------------------------------------------------
    Player 1 question: 4
    --------------------------------------------------
    An object is a(n) ______________.
    Enter the number for the correct answer: To exit enter "0"
    1: blueprint
    2: b. cookie cutter
    3: variable
    4: instance
    Your answer:4
    --------------------------------------------------
    Player 1 question: 5
    --------------------------------------------------
    By doing this you can hide a class’s attribute from code outside the class.
    Enter the number for the correct answer: To exit enter "0"
    1: avoid using the self parameter to create the attribute
    2: begin the attribute’s name with two underscores
    3: begin the name of the attribute with private__
    4: begin the name of the attribute with the @ symbol
    Your answer:2
    --------------------------------------------------
    --------------------------------------------------
    Your answers were: ['2', '4', '1', '4', '2']
    --------------------------------------------------
    Player: 1
    Question 1: The ______________ programming practice is centred on creating functions that are separate from the data that
    they work on.
    Correct answer: 2: procedural
    Your answer   : 2: procedural
    
    Question 2: The ______________ programming practice is centred on creating objects.
    Correct answer: 4: object-oriented
    Your answer   : 4: object-oriented
    
    Question 3: A(n) ______________ is a component of a class that references data.
    Correct answer: 3: data attribute
    Your answer   : 1: method ***Wrong***
    
    Question 4: An object is a(n) ______________.
    Correct answer: 4: instance
    Your answer   : 4: instance

    Question 5: By doing this you can hide a class’s attribute from code outside the class.
    Correct answer: 2: begin the attribute’s name with two underscores
    Your answer   : 2: begin the attribute’s name with two underscores
    
    --------------------------------------------------
    --------------------------------------------------
    Player 2 question: 1
    --------------------------------------------------
    A(n) ______________ method gets the value of a data attribute but does not change it.
    Enter the number for the correct answer: To exit enter "0"
    1: retriever
    2: constructor
    3: mutator
    4: accessor
    Your answer: 4

And so on


## 5. RetailItem Class ##

Write a class named `RetailItem` that holds data about an item in a retail
store. The class should store the following data in attributes:

*item description, units in inventory, and price.*

Once you have written the class, write a program that creates three `RetailItem`
objects and stores the following data in them:

|         |    Description | Units in Inventory |  Price |
|:--------|---------------:|-------------------:|-------:|
| Item #1 |         Jacket |                 12 |  59.95 |
| Item #2 | Designer Jeans |                 40 |  34.95 |
| Item #3 |          Shirt |                 20 |  24.95 |


## 7. Cash Register ##

This exercise assumes that you have created the `RetailItem` class for
Programming Exercise 5. Create a `CashRegister` class that can be used with the
`RetailItem` class. The `CashRegister` class should be able to internally keep
a list of `RetailItem` objects. The class should have the following methods:

 * A method named purchase_item that accepts a `RetailItem` object as an
   argument.
   Each time the purchase_item method is called, the RetailItem object that is
   passed as an argument should be added to the list.
 * A method named get_total that returns the total price of all the `RetailItem`
   objects stored in the `CashRegister` object’s internal list.
 * A method named show_items that displays data about the RetailItem objects
   stored in the `CashRegister` object’s internal list.
 * A method named clear that should clear the CashRegister object’s internal
   list.

Demonstrate the `CashRegister` class in a program that allows the user to select
several items for purchase. When the user is ready to check out, the program
should display a list of all the items he or she has selected for purchase, as
well as the total price.


## 8. Trivia Game ##

In this programming exercise you will create a simple trivia game for two
players. The program will work like this:

 * Starting with player 1, each player gets a turn at answering 5 trivia
   questions. (There should be a total of 10 questions.) When a question is
   displayed, 4 possible answers are also displayed. Only one of the answers
   is correct, and if the player selects the correct answer, he or she earns a
   point.
 * After answers have been selected for all the questions, the program displays
   the number of points earned by each player and declares the player with the
   highest number of points the winner.
   
To create this program, write a `Question` class to hold the data for a trivia
question. The `Question` class should have attributes for the following data:

 * A trivia question
 * Possible answer 1
 * Possible answer 2
 * Possible answer 3
 * Possible answer 4
 * The number of the correct answer (1, 2, 3, or 4)
 
The `Question` class also should have an appropriate `__init__` method,
accessors, and mutators.

The program should have a list or a dictionary containing 10 Question objects,
one for each trivia question. Make up your own trivia questions on the subject
or subjects of your choice for the objects.
