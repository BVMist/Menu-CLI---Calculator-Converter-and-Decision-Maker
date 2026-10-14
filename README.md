# Menu-CLI---Calculator-Converter-and-Decision-Maker

## About
This is a simple program that uses a command line interface(CLI). It includes a menu which gives the user access to three functions of the program namely a calculator, a converter and a decision maker.
A CLI is an interface that lets the user interact with the program via text/text command rather than buttons or icons as in GUIs(Graphical User Interface).
To make this program, I used various functionalities of python, like conditional statements with if-elif-else blocks and match. Loops to control the flow of the program. Functions and docstrings, dictionaries, variables and try and except for error handling.

## Calculator
This is a very simple calculator allowing for the most basic arithmetic operations namely addition, subtraction, multiplication and division.

Process: 
- It allows the user to choose the operation they'd like to perform (+, -, /, *) and takes the number to evaluate. 
- Then it evaluates it and print out the result. 
- It has error handling for operations not within it's capabilities and for invalid inputs such as non numbers.

Used: I used a while loop and the try and except blocks for the input validation. I used a function that performs the arithmetic operation and returns the answer. I used a match-case to match the operation to the different cases to get the desired evaluation. I also used variables to store input, and if and else statement for conditions.

Example Use:
Operation: +
First number: 1
Second number: 7
Ans: 8

Operation: /
First number: 2
Second number: 0
Cannot divide by zero.

## Converter 
This is a simple unit converter, that convert from one time unit to another. It only allows for conversion from and to second, minute, and hours.

Process: 
- It allows the user to input the starting and converting unit, limiting their choices to only that within its capabilities. 
- Then it gets the starting value from the user. 
- Then using the conversion table it has, it looks up the conversion factor and multiplies it with the value, displaying the result.

Used: I used a dictionary to store the conversion factor. Used a while loop with the try and except block for validating input. Used the if, else block for conditions. I also used a function that performs the conversion, dictionary methods and variables for storing input.

Example Use:
Starting unit: min
Unit to convert to: s
Value to convert: 2
Old value: 2.0min
New value: 120.0s

## Decision Maker
A simple program that takes in an age value and prints child, preteen, teen or adult based on the age range the age value falls into.

Process:
- It takes in and validate an age value and stores it in a variable called age.
- Then it calls the dec() function passing the age as an argument.
- The dec() function uses if and Elif statement to decide the current message to print out based on age range.
- Prints out the correct message.

Used: If-elif statement for decision making. While loop and try-except for error handling. Variable to store input and a function that makes the decision.

Example Use:
Case 1: Age(or exit to exit): 2
Child

Case 2: Age(or exit to exit): 15
Teen


## Conclusion
This project helped me practice more on using if-elif-else statements, while loops, try-except, functions, and building a CLI toolkit. I also learnt about match-case and how to use it.


### Video Links(YouTube)
- Test Run: https://youtube.com/shorts/DqDvWhrTYnM?si=oCmOFHsLZhB7wxVP
- Live Demo:
https://youtu.be/CZCwNqzbp08?si=o0s8ntMkwczc9G51
