"""
Day 2 Challenge: Anagram Checker
Problem Statement: Create a system to determine if two given strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once, while ignoring spaces, punctuation, and capitalization.

Examples:

☞Input: "Listen" and "Silent"

☞Output: Yes (They are anagrams)

☞Input: "A gentleman" and "Elegant man"

☞Output: Yes (They are anagrams)

☞Input: "Hello" and "World"

☞Output: No (They are not anagrams)
"""





import re

# Get user inputs
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

#Remove Symboles and convert to Lowercase
change_lower_1 = re.sub(r'[^A-Za-z0-9]', '', first_string).lower()
change_lower_2 = re.sub(r'[^A-Za-z0-9]', '', second_string).lower()

# Sort the characters in each string
sorted_first = sorted(change_lower_1)
sorted_second = sorted(change_lower_2)

# Compare the sorted strings
if sorted_first == sorted_second:
    print("Yes, they are anagrams!")
else:
    print("No, they are not anagrams.")
