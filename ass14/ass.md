# Programming Exercises #
## Assignment 12 Inheritance ##

This assignment will train Python: Inheritance, classes, objects - instances,
and subjects from the previous chapters. In the text book
"Starting Out with Python - 2nd Edition", do chapter 12: "Programming
Exercises":

  1, 2 and 3 and

Draw the UML graphic representation diagram for each of the involved classes
in exercises 1, 2 and 3 and draw the inheritance relationship that exists
between them.

## 1. Employee and ProductionWorker Classes ##

Write an Employee class that keeps data attributes for the following pieces of
information:

 * Employee name
 * Employee number

Next, write a class named ProductionWorker that is a subclass of the Employee
class. The ProductionWorker class should keep data attributes for the following
information:

 * Shift number (an integer, such as 1, 2, or 3)
 * Hourly pay rate
 
The workday is divided into two shifts: day and night. The shift attribute will
hold an integer value representing the shift that the employee works. The day
shift is shift 1 and the night shift is shift 2. Write the appropriate accessor
and mutator methods for each class. Once you have written the classes, write a
program that creates an object of the ProductionWorker class and prompts the
user to enter data for each of the object’s data attributes. Store the data in
the object and then use the object’s accessor methods to retrieve it and display
it on the screen.

## 2. ShiftSupervisor Class ##

In a particular factory, a shift supervisor is a salaried employee who
supervises a shift. In addition to a salary, the shift supervisor earns a yearly
bonus when his or her shift meets production goals. Write a ShiftSupervisor
class that is a subclass of the Employee class you created in Programming
Exercise 1. The ShiftSupervisor class should keep a data attribute for the
annual salary and a data attribute for the annual production bonus that a shift
supervisor has earned. Demonstrate the class by writing a program that uses a
ShiftSupervisor object.

## 3. Person and Customer Classes ##
Write a class named Person with data attributes for a person’s name, address, and tele-
phone number. Next, write a class named Customer that is a subclass of the Person class.
The Customer class should have a data attribute for a customer number and a Boolean data
attribute indicating whether the customer wishes to be on a mailing list. Demonstrate an
instance of the Customer class in a simple program.
