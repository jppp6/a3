"""
This module contains three functions: insertion(a_list), selection(a_list) and bubble(a_list).
These functions will sort the list passed to it using the sorting algorithm it is named after.

Author: Jean-Philippe Le Blanc
Section #: 002
Student #: 20157203
Date: October 25, 2021
"""

def insertion(a_list):
    outer, inner, swap = 0, 0, 0

    for key in range(1, len(a_list)):
        outer += 1
        i = key

        while i > 0 and a_list[i-1] > a_list[i]:
            a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
            inner +=1
            swap += 1
            i -= 1

    return (outer, inner, swap)

def selection(a_list):
    outer, inner, swap = 0, 0, 0
    
    for i in range(a_list):
        outer += 1
        min_idx = len(a_list) - 1

        for j in range(i, len(a_list)):
            inner += 1
            if a_list[j] < a_list[min_idx]:
                min_idx = j

        if min_idx != i:
            a_list[min_idx], a_list[j] = a_list[j], a_list[min_idx]
            swap += 1

    return (outer, inner, swap)

def bubble(a_list):
    outer, inner, swap = 0, 0, 0
    n, flag = len(a_list), True
    
    while flag:
        outer += 1
        flag = False
        for i in range (1, n):
            inner += 1
        
            if a_list[i-1] > a_list[i]:
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                flag = True
                swap += 1
        n -= 1

    return (outer, inner, swap)