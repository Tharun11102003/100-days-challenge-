"""
Task: FizzBuzz
Problem Statement: Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
Steps:
1.	Input: No input required.
2.	Process:
    o Loop through numbers from 1 to 100.
    o For each number:
	    Print "Fizz" if the number is divisible by 3.
	    Print "Buzz" if the number is divisible by 5.
	    Print "FizzBuzz" if the number is divisible by both 3 and 5.
	    Otherwise, print the number itself.
3.	Output: The sequence from 1 to 100 with the specified replacements.

"""


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
