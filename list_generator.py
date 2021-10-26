"""
This module contains three functions: list_ascending(a_length), list_descending(a_length) and list_randomized(a_length).
These functions will generate lists with data ordered according to the name of the function.

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: October 25, 2021
"""

# Import random module as r
import random as r

# Function that creates an ascending list based on the length passed to it
def list_ascending(a_length):
    #List comprehensions using r.uniform to generate random floats within a certain range at each step
    return [round(r.uniform(x, x+10), 2) for x in range(1, a_length*10, 10)]

# Function that creates a descending list based on the length passed to it
def list_descending(a_length):
    # List comprehensions using r.uniform to generate random floats within a certain range at each step
    return [round(r.uniform(x, x+10), 2) for x in range(a_length*10, 1, -10)]

# Function that creates a randomized list based on the length passed to it
def list_randomized(a_length):
    # List comprehensions using r.uniform to generate random floats 
    return [round(r.uniform(1, a_length*10), 2) for x in range(a_length)]