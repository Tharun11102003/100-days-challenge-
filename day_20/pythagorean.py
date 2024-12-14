"""
Task: Check for a Pythagorean Triplet
Problem Statement:
Write a Python function to check if three numbers form a Pythagorean triplet (i.e., a^2 + b^2 = c^2).

Steps:
1. Input:
The user enters three numbers.

2. Process:
Define a function is_pythagorean_triplet(numbers) that:

Checks if the list has exactly three numbers.

Sorts the numbers to find the smallest (a), middle (b), and largest (c).

Checks if 
a^2 + b^2 = c^2.

Returns True if they form a triplet, otherwise False.

Get the user input and convert it to a list of integers.

Call the function with the input list.

Print whether the numbers form a Pythagorean triplet or not.
"""




def is_pythagorean_triplet(numbers):
    if len(numbers) != 3:
        return False
    a, b, c = sorted(numbers)
    return a**2 + b**2 == c**2

numbers = list(map(int, input("Enter three numbers separated by space: ").split()))
if is_pythagorean_triplet(numbers):
    print(f"{numbers} form a Pythagorean triplet.")
else:
    print(f"{numbers} do not form a Pythagorean triplet.")
