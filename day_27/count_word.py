"""
Task: Simple Word Counter
✿ Problem Statement:
Write a Python program to create a simple word counter that counts the number of words in a given text input by the user.

★ Steps:
    1. Input:
        ❖ The user provides a text input.

    2. Process:
        ❖ Define a function count_words(text) that:

        ※ Split the Text:
            ● Use the split() method to break the text into words based on whitespace.

        ※ Count the Words:
            ● Use the len() function to count the number of words in the resulting list.

        ※ Return the Word Count:
            ● Return the count of words.

    3. Output:
        ❖ Display the word count based on the user input.
"""


def count_words(text):

    words = text.split()

    return len(words)

def main():

    text = input("Enter a text: ")

    word_count = count_words(text)

    print(f"Word Count: {word_count}")


main()
