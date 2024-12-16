"""
Task: Find the Missing Number

✿ Problem Statement: Write a Python program to find the missing number in a given list of integers from 1 to n. The list contains n-1 integers, and each integer is unique.

★ Steps:

1.Input: 
    ❖ The user provides a list of integers from 1 to n, with one number missing.

2.Process: 
    ❖ Define a function find_missing_number(nums, n) that:

    ❖ Calculate the Expected Sum: - Use the formula for the sum of the first n natural numbers: 
        Sum = n * (n + 1) // 2

    ❖ Calculate the Actual Sum: - Sum the elements of the given list.

    ❖ Find the Missing Number: - Subtract the actual sum from the expected sum to get the missing number.

Output: 
    ❖ Display the missing number.
"""




def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


nums = [1, 2, 4, 5, 6]
n = 6
missing_number = find_missing_number(nums, n)
print("Missing Number:", missing_number)
