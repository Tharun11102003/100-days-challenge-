"""
Task: Find the Intersection of Two Lists
✿ Problem Statement:
Write a Python program to find the intersection of two given lists. The program should take two lists as input and return a new list containing the elements that are common to both lists.

★ Steps:
    1. Input:
        ❖ The user provides two lists.

    2. Process:
        ❖ Define a function find_intersection(list1, list2) that:
            ✥ Convert Lists to Sets: ※ Convert both lists to sets to leverage set operations.
            ✥ Find the Intersection: ※ Use the intersection operation to find common elements between the two sets.
            ✥ Convert the Result to a List: ※ Convert the resulting set back to a list to get the final intersection list.
            ✥ Return the Intersection List: ※ Return the list containing the common elements.

    3. Output:
        ❖ Display the intersection of the two lists.
"""



def find_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    return intersection


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print("Intersection:", result)











#=======================================