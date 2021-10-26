"""
This program asks the user for the length of the list desired. It then generates three lists of that length, one in ascending, descending and randomized order.
These three new lists are then passed to three sorting algorithms, insertion sort, selection sort and bubble sort.
The results (the amount of swaps, inner loop iterations and outer loop iterations) are then displayed for all three lists for the user to see.

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: October 25, 2021
"""

# Import the functions from the modules created for this assignment (list_generator and quadratic_sorts)
from list_generator import *
from quadratic_sorts import *

# main() function takes care of running the program
def main():
    length = int(input("Please enter the length of input lists: ")) # Get the desired length of the list from the user


    l_best = list_ascending(length) # Use list_ascending function to generate the best case list
    l_worst = list_descending(length) # Use list_descending function to generate the worst case list
    l_rand = list_randomized(length) # Use list_randomized function to generate a randomized list
  
    
    print(f"\nBest-case example: {l_best}") # Print the best case list
    print(f"Worst-case example: {l_worst}") # Print the worst case list
    print(f"Randomized example: {l_rand}") # Print the randomized list


    insBest_outer, insBest_inner, insBest_swap = insertion(l_best) # Perform the insertion sort on the best case list and store the inner, outer and swap variables
    insWorst_outer, insWorst_inner, insWorst_swap = insertion(l_worst) # Perform the insertion sort on the worst case list and store the inner, outer and swap variables
    insRand_outer, insRand_inner, insRand_swap = insertion(l_rand) # Perform the insertion sort on the randomized list and store the inner, outer and swap variables
    print("\n\nUsing insertion sort: ") # Let the user know which sorting algorithm is being used next
    print("           # of outer loops   # of inner loops   # of swaps") # Print the columns of the table
    print(f"Best-case:        {insBest_outer}                 {insBest_inner}               {insBest_swap}") # Print results of the best case
    print(f"Worst-case:       {insWorst_outer}                 {insWorst_inner}              {insWorst_swap}") # Print results of the worst case
    print(f"Randomized-case:  {insRand_outer}                 {insRand_inner}               {insRand_swap}") # Print results of the randomized case
    

    selBest_outer, selBest_inner, selBest_swap = selection(l_best) # Perform the selection sort on the best case list and store the inner, outer and swap variables
    selWorst_outer, selWorst_inner, selWorst_swap = selection(l_worst) # Perform the selection sort on the worst case list and store the inner, outer and swap variables
    selRand_outer, selRand_inner, selRand_swap = selection(l_rand) # Perform the selection sort on the randomized list and store the inner, outer and swap variables
    print("\n\nUsing selection sort: ") # Let the user know which sorting algorithm is being used next
    print("           # of outer loops   # of inner loops   # of swaps") # Print the columns of the table
    print(f"Best-case:        {selBest_outer}                 {selBest_inner}              {selBest_swap}") # Print results of the best case
    print(f"Worst-case:       {selWorst_outer}                 {selWorst_inner}              {selWorst_swap}") # Print results of the worst case
    print(f"Randomized-case:  {selRand_outer}                 {selRand_inner}              {selRand_swap}") # Print results of the randomized case

    
    bubBest_outer, bubBest_inner, bubBest_swap = bubble(l_best) # Perform the bubble sort on the best case list and store the inner, outer and swap variables
    bubWorst_outer, bubWorst_inner, bubWorst_swap = bubble(l_worst) # Perform the bubble sort on the worst case list and store the inner, outer and swap variables
    bubRand_outer, bubRand_inner, bubRand_swap = bubble(l_rand) # Perform the bubble sort on the randomized list and store the inner, outer and swap variables
    print("\n\nUsing bubble sort: ") # Let the user know which sorting algorithm is being used next
    print("           # of outer loops   # of inner loops   # of swaps") # Print the columns of the table
    print(f"Best-case:        {bubBest_outer}                 {bubBest_inner}               {bubBest_swap}") # Print results of the best case
    print(f"Worst-case:       {bubWorst_outer}                 {bubWorst_inner}              {bubWorst_swap}") # Print results of the worst case
    print(f"Randomized-case:  {bubRand_outer}                 {bubRand_inner}              {bubRand_swap}") # Print results of the randomized case

    return

main() # main() call to start the program