"""
Task: Binary Search Algorithm

✿ Problem Statement: Write a Python function to implement binary search. Given a sorted list of integers and a target value, the function should return the index of the target value if it is present in the list. If the target value is not present, the function should return -1.

★ Steps:
    1.Input:
       ❖ Provide a sorted list of integers (list) and a target value (target).

    2.Initialization:
       ❖ Set up two pointers, left and right, to represent the current search range.
       ❖ left starts at index 0 and right starts at the last index of the list.

    3.Process:
       ❖ While left is less than or equal to right:
           ※ Calculate the middle index (mid).
           ※ Compare the value at the middle index (list[mid]) with the target:
               ● If list[mid] equals the target, return the middle index.
               ● If list[mid] is less than the target, move left to mid + 1.
               ● If list[mid] is greater than the target, move right to mid - 1.

    4.Output:
       ❖ If the target is not found in the list, return -1.
"""



def binary_search(list, target):
    left, right = 0, len(list) - 1
 
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binary_search([5, 15, 25, 35, 45, 55, 65], 45))



#============================













