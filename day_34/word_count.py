"""
Task: Count Words in a String
✿ Problem Statement: Write a Python program that takes a string as input and counts the number of words in that string. The program should only count words if the string contains alphabetic characters and spaces. If the string contains any numbers or symbols, the program should return False.

★ Steps:

    1.Input:
       ❖ The user provides a string, which can be a sentence or a block of text (e.g., 'Hello world').

    2.Process:
       ❖ Check for Valid Input:
           ● Ensure that the input string only contains alphabetic characters and spaces.
           ● Use a generator expression to check each character in the string.

       ❖ Split the Text into Words:
           ● If the input is valid, use the .split() method to split the string into individual words.
           ● This method splits the text at whitespace characters (spaces, tabs, newlines, etc.).

       ❖ Count the Words:
           ● Use the len() function to count the number of words in the list created by the .split() method.

       ❖ Handle Invalid Input:
           ● If the input contains any numbers or symbols, return False.

    Output:
       ❖ If the input is valid, display the number of words in the string.
       ❖ If the input is invalid, display an error message
"""


def count_words(text):
    if all(char.isalpha() or char.isspace() for char in text):
        words = text.split()
        return len(words)
    else:
        return False

user = input("Enter the sentence: ")
result = count_words(user)
if result is False:
    print("User should only provide a sentence with alphabetic characters and spaces.")
else:
    print(f"Number of Words: {result}")







#===========================


