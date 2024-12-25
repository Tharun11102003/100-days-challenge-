"""
Task: Check If a Number Is a Harshad Number 
✿ Problem Statement: 
    Write a Python program that takes a positive integer as input and determines if it is a Harshad number. A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.

★ Steps:
    1. Input:
        ❖ The user provides a positive integer.

    2. Process:
        ❖ Define a function to check if the number is a Harshad number:
            ※ Extract Digits: - Initialize Variables: 
                ● Start by initializing original_number to store the original input number. 
                ● Create an empty list digits to store the digits of the number. 
                ● Initialize digit_sum to 0 to store the sum of the digits.

            ※ Extract and Store Digits: 
                ● Use a while loop to extract each digit of the number by taking the remainder when divided by 10 (using the modulo operator %). 
                ● Append each extracted digit to the list digits. 
                ● Update the number by performing integer division by 10 to remove the last digit (using the // operator).

            ※ Calculate the Sum of Digits: - Sum the Digits: 
                ● Use the sum() function to calculate the sum of the digits stored in the list digits.

            ※ Check Divisibility: - Compare the Original Number with the Sum of Its Digits: 
                ● Check if the original_number is divisible by digit_sum using the modulo operator %.

            ※ Determine If the Number Is a Harshad Number: 
                ● If the original_number is divisible by digit_sum, print that the number is a Harshad number. 
                ● Otherwise, print that the number is not a Harshad number.

3. Output:
❖ Display a message indicating whether the given number is a Harshad number or not.
"""





number = int(input("Enter the number: "))
original_number = number
digits = []
digit_sum = 0

while number > 0:
    digit = number % 10
    digits.append(digit)
    number = number // 10

digit_sum = sum(digits)

if original_number % digit_sum == 0:
    print("Harshad number")
else:
    print("Not Harshad number")
