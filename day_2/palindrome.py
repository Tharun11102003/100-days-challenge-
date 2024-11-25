"""
Day 2 Challenge: Palindrome Checker
Problem Statement: Create a system to determine whether a given string is a palindrome. A palindrome reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization.

Examples:

1. "Madam" -> True

2. "A man, a plan, a canal, Panama" -> True

3. "Hello, World!" -> False
"""




#import the regular expressions module
import re

#Get user to input
user_input = input("Enter the String or Num : ")

#Remove Symboles and convert to Lowercase
change_value = re.sub(r'[^A-Za-z0-1]',"",user_input).lower()

#Index to reverse the String
palindrome = change_value[::-1]

# If else method to check the palindrome
if change_value == palindrome:
    print("True")
else:
    print("False")

