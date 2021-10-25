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

A3_2 Quadratic sorts

Write a program A3_2 that compares the efficiency of the three quadratic sorting algorithms discussed in the lectures. 

Upon execution, your program will ask the user to enter the number of items in the input list of floats. Then it will generate one sorted list in ascending order, i.e., the best case, one sorted list in descending order, i.e., the worst case, and one randomized list. It will then show, for each sorting algorithm, the number of outer loop executions, the number of inner loop executions, and the number of swaps in the best case, the worst case, and the randomized case.

Your program A3_2 should have a main() function and may include other functions that you prefer. The execution section of your program should only include one instruction that calls main().

You also need to submit two modules:

Module quadratic_sorts.py that includes three functions: insertion(a_list), selection(a_list), and bubble(a_list);

Module list_generator.py that includes three functions: list_ascending(a_length), list_descending(a_length), list_randomized(a_length).

An example output of running program A3_2 is shown below.

 

Please enter the length of input lists: 5

 

Best-case example: ['1.69', '22.27', '33.46', '46.11', '68.40']

Worse-case example: ['88.22', '77.66', '52.13', '16.76', '9.10']

Randomized example: ['2.27', '1.66', '13.60', '1.59', '1.02']

 

Using insertion sort:

                        # of outer loops   # of inner loops   # of swaps

Best-case                     4                      0                      0

Worst-case                  4                      10                    10

Randomized-case       4                      8                      8

 

Using selection sort:

                        # of outer loops   # of inner loops   # of swaps

Best-case                     4                      10                    0

Worst-case                  4                      10                    2

Randomized-case       4                      10                    4

 

Using bubble sort:

                        # of outer loops   # of inner loops   # of swaps

Best-case                     1                      4                      0

Worst-case                  5                      20                    10

Randomized-case       5                      20                    8

  