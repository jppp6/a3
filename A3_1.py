"""
This program uses the logic of a binary search to try to guess the users imaginary number within log2(upper_bound-lower_bound) + 1 questions.

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: October 25, 2021
"""

# main() function takes care of running the program
def main():
    lower = int(input("Please enter the lower bound: ")) # Ask the user for the lower bound 
    upper = int(input("Please enter the upper bound: ")) # Ask the user for the upper bound 

    while lower <= upper: # While loop that runs while lower is smaller or equal to upper
        mid = (upper + lower)//2 # Calculate the mid point 
        answer = input(f"Is your number greater than {mid} (Y/N)? ") # Ask the user if the number is greater than the value of mid
        
        if answer in ["y", "Y", "yes", "Yes"]: # If answer was yes
            lower = mid + 1 # Change the lower bound to the value of mid + 1
        else: # The answer was no
            upper = mid - 1 # Change the upper bound to the value of mid - 1

    print(f"The number you had in mind was {mid}") # Print final message with the number the computer guessed

main() # main() call to start the program