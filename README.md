# Menu-CLI---Calculator-Converter-and-Decision-Maker

## About
This is a simple program that uses a command line interface(CLI). It includes a menu which gives the user access to three functions of the program namely a calculator, a converter and a decision maker.
A CLI is an interface that lets the user interact with the program via text/text command rather than buttons or icons as in GUIs(Graphical User Interface).
To make this program, I used various functionalities of python, like conditional statements with if-elif-else blocks and match. Loops to control the flow of the program. Functions and docstrings, dictionaries, variables and try and except for error handling.

## Calculator
This is a very simple calculator allowing for the most basic arithmetic operations namely addition, subtraction, multiplication and division.

Process: It allows the user to choose the operation they'd like to perform (+, -, /, *) and takes the number to evaluate. Then it evaluates it and print out the result. 
It has error handling for operations not within it's capabilities and for invalid inputs such as non numbers.

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

Process: It allows the user to input the starting and converting unit, limiting their choices to only that within its capabilities. Then it gets the starting value from the user. Then using the conversion table it has, it looks up the conversion factor and multiplies it with the value, displaying the result.
