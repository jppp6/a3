"""
This module contains three functions: insertion(l), selection(l) and bubble(l).
These functions will sort the list passed to it using the sorting algorithm it is named after.

Author: Jean-Philippe Le Blanc 
Section #: 002
Student #: 20157203
Date: October 25, 2021
"""

# Function that performs an insertion sort on the list passed to it
def insertion(l):
    # Initialize all the variables required: 'outer', 'inner' and 'swap' are all set to 0
    # Copy 'l' using list() function to create a new copy of the list as 'a_list'
    a_list, outer, inner, swap = list(l), 0, 0, 0

    for key in range(1, len(a_list)): # for-loop to iterate through the list
        outer += 1 # Increment the outer loop counter
        i = key # Copy the value of 'key' to 'i'

        while i > 0 and a_list[i-1] > a_list[i]: # while loop that continues while: 'i' is greater than 0 AND the previous element in the list is bigger than the current element
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1] # Swap the elements at position 'i' and 'i-1'
            inner +=1 # Increment the inner loop counter
            swap += 1 # Increment the swap counter
            i -= 1 # Decrement 'i'

    return outer, inner, swap # Return 'outer', 'inner' and 'swap' 

# Function that perfroms a selection sort on the list passed to it
def selection(l):
    # Initialize all the variables required: outer, inner and swap are all set to 0
    # Copy l using list() function to create a new copy of the list as a_list
    # Set n as the length of a_list
    a_list, outer, inner, swap = list(l), 0, 0, 0
    n = len(a_list)

    for i in range(n-1): # for-loop that goes through the entire list
        outer += 1 # Increment the outer loop counter
        min = i # Set 'min' to the value of 'i'

        for j in range(i+1, n): # for-loop to find the smallest element in the list
            inner += 1 # Increment the inner loop counter
            if a_list[j] < a_list[min]: # Check to see if entry 'j' is smaller than entry 'min'
                min = j # It is, so change 'min' to 'j'

        if min != i: # Check to see if min is different than i
            a_list[min], a_list[i] = a_list[i], a_list[min] # It is, swap the elements at position 'min' and 'i'
            swap += 1 # Increment the swap counter 

    return outer, inner, swap # Return 'outer', 'inner' and 'swap' 


# Function that performs a bubble sort on the list passed to it
def bubble(l):
    # Initialize all the variables required: 'outer', 'inner' and 'swap' are all set to 0, 'flag' is set to True
    # Copy 'l' using list() function to create a new copy of the list as 'a_list'
    # Set 'n' as the length of 'a_list'
    a_list, flag, outer, inner, swap = list(l), True, 0, 0, 0
    n = len(a_list)
    
    while flag: # While the condition flag is True
        outer += 1 # Increment the outer loop counter
        flag = False # Set 'flag' to False

        for i in range (1, n): # for-loop to iterate through elements 1 to 'n'
            inner += 1 # Increment the inner loop counter
        
            if a_list[i-1] > a_list[i]: # Compare the entry at 'i' if it is smaller than at 'i-1'
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i] # It is, swap elements at position 'i' and 'i-1'
                flag = True # Set 'flag' to True
                swap += 1 # Increment the swap counter
                
        n -= 1 # Decrement 'n'

    return outer, inner, swap # Return 'outer', 'inner' and 'swap' 