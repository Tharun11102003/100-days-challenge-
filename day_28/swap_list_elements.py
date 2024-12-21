"""
Task: Swap Two Elements in a List 
✿ Problem Statement:
Write a Python program to swap two elements in a given list. The program should take a list and the indices of the two elements to be swapped as input and return the modified list.

★ Steps:
    1. Input:
        ❖ The user provides a list of elements and the indices of the two elements to be swapped.

    2. Process:
        ❖ Define a function swap_elements(lst, index1, index2) that:

            ※ Check Indices: ● Ensure that the provided indices are within the valid range of the list.

            ※ Swap the Elements: ● Use tuple unpacking to swap the elements at the given indices.

            ※ Return the Modified List: ● Return the list after the elements have been swapped.

    3. Output:
        ❖ Display the modified list after swapping the elements.
"""



def swap_elements(lst, index1, index2):

    if index1 >= len(lst) or index2 >= len(lst):
        print("Error: One or both indices are out of range.")
        return lst

    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

index1 = 1
index2 = 3

modified_list = swap_elements(my_list, index1, index2)
print("Modified List:", modified_list)






#==========================