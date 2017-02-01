# Programming Exercises #
## Assignment 11 Classes and objects ##

This assignment will train Python: classes, objects - instances and subjects
from the previous chapters.
In the text book “Starting Out with Python - 2nd Edition”,
do chapter 11: “Programming Exercises”:

 1, 2, 3 and 4.

Draw the UML graphic representation/UML diagram for each of the involved classes
in exercises 1 and 2.

### 1. Pet Class ###

Write a class named Pet, which should have the following data attributes:
 
 * `__name` (for the name of a pet)
 * `__animal_type` (for the type of animal that a pet is. Example values are
                   ‘Dog’, ‘Cat’, and ‘Bird’)
 * `__age` (for the pet’s age)
 
The Pet class should have an `__init__` method that creates these attributes. It
should also have the following methods:

 * `set_name`: This method assigns a value to the _ _name field.
 * `set_animal_type`: This method assigns a value to the _ _animal_type field.
 * `set_age`: This method assigns a value to the _ _age field.
 * `get_name`: This method returns the value of the name field.
 * `get_type`: This method returns the value of the type field.
 * `get_age`: This method returns the value of the age field.
 
Once you have written the class, write a program that creates an object of the
class and prompts the user to enter the name, type, and age of his or her pet.
This data should be stored as the object’s attributes. Use the object’s accessor
methods to retrieve the pet’s name, type, and age and display this data on the
screen.

### 2. Car Class ###

Write a class named Car that has the following data attributes:

 * `__year_model`: (for the car’s year model)
 * `__make` (for the make of the car)
 * `__speed` (for the car’s current speed)

The Car class should have an `__init__` method that accept the car’s year model
and make as arguments. These values should be assigned to the object’s
`__year_model` and `__make` data attributes. It should also assign 0 to the
`__speed` data attribute.

The class should also have the following methods:
 * `accelerate`: The `accelerate` method should add 5 to the speed data
                 attribute each time it is called.
 * `brake`: The brake method should subtract 5 from the speed data attribute
            each time it is called.
 * `get_speed`: The get_speed method should return the current speed.

Next, design a program that creates a Car object, and then calls the accelerate
method five times. After each call to the accelerate method, get the current 
speed of the car and display it. Then call the brake method five times. After
each call to the brake method, get the current speed of the car and display it.

### 3. Personal Information Class ###

Design a class that holds the following personal data: name, address, age, and
phone number. Write appropriate accessor and mutator methods. Also, write a
program that creates three instances of the class. One instance should hold your
information, and the other two should hold your friends’ or family members’
information.

### 4. Employee Class ###

Write a class named Employee that holds the following data about an employee in
attributes: name, ID number, department, and job title.

Once you have written the class, write a program that creates three Employee objects to
hold the following data:

| Name         | ID Number | Department    | Job Title       |
| -------------|:---------:|--------------:|----------------:|
| Susan Meyers |   47899   | Accounting    | Vice President  |
| Mark Jones   |   39119   | IT            | Programmer      |
| Joy Rogers   |   81774   | Manufacturing |  Engineer       |

The program should store this data in the three objects and then display the 
data for each employee on the screen.
