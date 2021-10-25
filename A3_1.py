# https://onq.queensu.ca/d2l/lms/dropbox/user/folder_submit_files.d2l?db=257360&grpid=0&isprv=0&bp=0&ou=578430

"""
This program 

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: 

"""

# main() function takes care of running the program
def main():
    try:
        lower = int(input("Please enter the lower bound: ")) # Ask the user for the lower bound 
        upper = int(input("Please enter the upper bound: "))
    except ValueError:
        print("Please input an integer.")
        

    while lower <= upper:
        mid = (upper + lower)//2 
        a = input(f"Is your number greater than {mid} (Y/N)? ")
        
        if a in ["y", "Y", "yes", "Yes"]:
            lower = mid + 1
        else: 
            upper = mid - 1

    print(f"The number you had in mind was {mid}")     
        
    return 0

main() # main() call to start the program