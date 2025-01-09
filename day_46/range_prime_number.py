"""
Task: Identify prime numbers in a given range.

Problem Statement: Given a range of integers from start_number to end_number, identify and print all the prime numbers within that range.

Steps:
    1.Input: 
        ❖ Two integers, start_number and end_number, which define the range of numbers to check for primality.

    2.Process: 
        ❖ Initialize a variable, is_prime, to 0. This variable will be used to flag whether a number is prime. 
        ❖ Iterate through each number, current_number, in the range from start_number to end_number (inclusive). 
        ❖ For each current_number, iterate through all possible divisors, divisor, from 2 up to (but not including) current_number. 
        ❖ Check if the current_number is divisible by any divisor in the inner loop. If it is, set is_prime to 1. 
        ❖ If the is_prime flag remains 0 after checking all divisors, it means the current_number is a prime number. Print the current_number. 
        ❖ Reset the is_prime flag to 0 for the next current_number.

    3.Output: 
        ❖ The prime numbers within the specified range.
"""

start_number = 1
end_number = 20
is_prime = 0

for current_number in range(start_number, end_number + 1):
    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            is_prime = 1
    if is_prime == 0:
        print(current_number)
    is_prime = 0


#===============================================