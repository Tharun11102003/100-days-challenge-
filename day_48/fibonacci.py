"""
Task: Generate a Fibonacci Sequence
Problem Statement:
You want to generate the Fibonacci sequence up to a specified number of terms. The Fibonacci sequence is a series of numbers where each number (after the first two) is the sum of the two preceding ones. The sequence starts with 0 and 1.

Steps:
    1.Input:
       ❖ You need an integer representing the number of terms in the Fibonacci sequence.

    2.Process:
       ❖ Initialize variables for the first two terms of the sequence, which are 0 and 1.
       ❖ Create an empty list to store the generated sequence.
       ❖ Use a loop to iterate from 0 to the specified number:
           ※ For the first term (i == 0), add 0 to the list.
           ※ For the second term (i == 1), add 1 to the list.
           ※ For subsequent terms, calculate the next term by adding the two previous terms, update the variables accordingly, and add the new term to the list.
       ❖ Continue this process until the specified number of terms is generated.

    3.Output:
       ❖ The result will be a list containing the Fibonacci sequence up to the specified number of terms.
"""


number = int(input("enter :"))
second = 1
first = 0 
sum_values = 0 
sequence = []
for i in range(0, number):
    if i == 0:
        sequence.append(first)
    elif i == 1:
        sum_values = second + first
        sequence.append(sum_values)
    else:
        second = sum_values
        sum_values += first
        first = second
        sequence.append(sum_values)
print(sequence)
