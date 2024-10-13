"""Implementing Algorithms to Practice Computational Thinking"""

__author__ = "730521229"


def all(list_ints: list[int], integer: int) -> bool:
    """Indicates whether or not all the ints in the list are the same as given int"""
    if len(list_ints) == 0: #if list is empty, do this
        return False
    
    for num in list_ints: #checks each int in list
        if num != integer: #if a value in list != to given int, do this
           return False
    return True #if all equal to given int, do this

def max(input: list[int]) -> int:
    """Returns largest integer in the list"""
    if len(input) == 0: #if list is empty, raise a ValueError
        raise ValueError("max() arg is an empty List")
    
    largest_int = input[0] #Makes first item in list the largest to start
    for num in input: #looks through list
        if num > largest_int: #if current item the largest, replace largest variable with current
            largest_int = num
    return largest_int #after looking through entire list, rteurn the largest int

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if 2 provided lists are identical"""
    if len(list_1) != len(list_2): #checks if lists are same size
        return False #if they are not, do this
    index = 0 #sets initial index
    for num in list_1: #looks through each item in list 1
        if num != list_2[index]: #if integers of same index is not equal in each corresponding list...
            return False #do this
        index += 1 #changes index for list 2 in next iteration so they match
    return True #if lists are identical, do this

def extend(list_1: list[int], list_2: list[int]) -> None:
    """Mutates list 1 by adding all the elements from the 2nd list"""
    for num in list_2: #looks through each item in 2nd list
        list_1. append(num) #add each item in list 2 to list 1 individually
