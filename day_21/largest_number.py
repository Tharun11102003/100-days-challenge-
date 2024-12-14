"""
Task: Find the Largest Number in a List

 ✿ Problem Statement: Write a Python program to find the largest number in a given list of numbers.

★ Steps:

1.Input:

    ❖The user provides a list of numbers.

2.Process:

    ❖Define a function find_largest_number(numbers) that:

        ✥Checks if the list is empty:

            ※If the list is empty, return None or an appropriate message.

        ✥Initialize the largest number:

            ※Assume the first number in the list is the largest.

        ✥Iterate through the list:

            ※Compare each number with the current largest number.

            ※Update the largest number if a larger number is found.

        ✥Return the largest number:

            ※After completing the iteration, return the largest number found in the list.
"""


def find_largest_number(numbers):
    if not numbers:
        return None  
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


numbers = [10, 250, 50, 25, 100, 45]
result =  find_largest_number(numbers)
print("The largest number is:", result)
