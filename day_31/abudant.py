"""
Task: Check If a Number Is an Abundant Number
✿ Problem Statement: Write a Python program that takes a positive integer as input and determines if it is an abundant number. An abundant number is a number that is smaller than the sum of its proper divisors (excluding itself).

★ Steps:
    1.Input: 
        ❖ The user provides a positive integer.

    2.Process: 
        ❖ Define a function to check if the number is abundant:
            ※ Initialize the Sum of Divisors: 
                ● Start by initializing a variable divisor_sum to 1. The number 1 is a proper divisor for all positive integers.

            ※ Find Proper Divisors: 
                ● Iterate through the range from 2 to the given number (exclusive). ● For each number i in this range, check if i is a divisor of the given number. If it is, add i to divisor_sum.

            ※ Compare the Sum to the Number: 
                ● After finding and summing all proper divisors, compare divisor_sum to the given number.

            ※ Determine If the Number Is Abundant: 
                ● If divisor_sum is greater than the given number, print that the number is an abundant number. ● Otherwise, print that the number is not an abundant number.

    3.Output: ❖ Display a message indicating whether the given number is an abundant number or not.
"""



number = int(input("Enter a number: "))

divisor_sum = 1

for i in range(2, number):
    if number % i == 0: 
        divisor_sum += i

if divisor_sum > number:
    print(number, 'is an Abundant Number')
else:
    print(number, 'is not an Abundant Number')





#========================