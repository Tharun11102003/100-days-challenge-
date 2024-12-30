"""
Task: Find the Greatest Common Divisor (GCD) of Two Numbers
✿ Problem Statement: Write a Python function to find the greatest common divisor (GCD) of two integers. The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder.

Steps:
    1.Input:
       ❖ Provide two integers a and b to the function.

    2.Using the Euclidean Algorithm:
       ❖ The Euclidean algorithm is based on the principle that the GCD of two numbers also divides their difference.
       ❖ Continue to divide the larger number by the smaller number and update the numbers until the remainder is zero.

    3.Steps in the Function:
       ❖ Initialize: Start with the two input numbers a and b.
       ❖ Loop: 
           ● Use a while loop to iterate until b becomes zero.
           ● Inside the loop, update a and b using the Euclidean algorithm: a, b = b, a % b.
           ● This updates a to be the current value of b, and b to be the remainder when a is divided by b.

       ❖ Return the GCD: When the loop exits (i.e., b is zero), a holds the GCD of the original numbers.

    4.Output:
       ❖ Return the GCD of the two input numbers.
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 48
b = 18
print(gcd(a, b)) 

a = 56
b = 98
print(gcd(a, b))
