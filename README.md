# Assignment 3 for CISC 121
A3_1 Binary search 

Write a program that determines an integer value the user had in mind. Your program first asks the user to enter the lower and upper bounds of the range that the integer belongs to, and then presents a series of questions “Is the number greater than x?” with yes/no answers to the user in order to determine the integer value that the user had in mind. 

For instance, if the integer in mind is 5 and the interaction between the user and your program is:

Please enter the lower bound: -10

Please enter the upper bound: 50

Is the number greater than 20 (Y/N)? n

Is the number greater than 4 (Y/N)? y

Is the number greater than 12 (Y/N)? n

Is the number greater than 8 (Y/N)? n

Is the number greater than 6 (Y/N)? n

Is the number greater than 5 (Y/N)? n

Your program should then print:

The number you had in mind is 5

 

Your program should ask no more than  questions . Your program A3_1.py should include a main() function and may include other functions that you prefer. The execution section of your program should only include one instruction that calls main().