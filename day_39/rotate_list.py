"""
Task: Rotate a List Using Its Reversed Elements
Problem Statement:
Write a Python function to rotate a list by inserting elements from its reversed version at the front of the list for a specified number of rotations.

Steps:
    1.Input:
       ❖ Start with a list of numbers called original_list.
       ❖ Specify the number of rotations with a variable called rotation_count.

    2.Algorithm:
       ❖ Reverse the original list to get reversed_list.
       ❖ For each rotation, insert an element from reversed_list at the start of original_list and remove the last element of original_list to keep its length the same.

    3.Steps in the Code:
       ❖ Initialize:
           ● Create a list original_list with the given numbers: [1, 2, 3, 4, 5, 6, 7].
           ● Set the number of rotations with rotation_count to 3.
           ● Reverse the original_list to get reversed_list: [7, 6, 5, 4, 3, 2, 1].

       ❖ Loop:
           ● Use a for loop to repeat the rotation process 3 times (rotation_count times).
           ● In each iteration:
               ⁕ Insert an element from reversed_list at the front of original_list.
               ⁕ Remove the last element of original_list to keep the list length unchanged.

    4.Output:
       ❖ After completing the rotations, print the modified original_list
"""


original_list = [1, 2, 3, 4, 5, 6, 7]
rotation_count = 3
reversed_list = original_list[::-1]

for i in range(0, rotation_count):
    original_list.insert(0, reversed_list[i % len(reversed_list)])
    original_list.pop()

print(original_list)
