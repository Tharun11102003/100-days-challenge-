"""
Task: Find the First Unique Character in a String
✿ Problem Statement: Write a Python function to find the first unique character in a string. The function should return the index of the first character that does not repeat. If there is no unique character, return -1.

Steps:
    1. Input:
        ❖ Provide a string s to the function.

    2. Count Frequencies:
        ❖ Create a dictionary char_count to store the frequency of each character in the string. 
        ❖ Iterate through each character in the string s and update the count in the char_count dictionary.

    3. Find First Unique Character:
        ❖ Iterate through the string s again. 
        ❖ For each character, check its count in the char_count dictionary. 
        ❖ If the count is 1, return the index and the character.

    4. Output:
        ❖ If a unique character is found, return its index and the character. 
        ❖ If no unique character is found, return -1 and None.
"""



def first_unique_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index, char

    return -1, None

s = "leetcode"
index, unique_char = first_unique_char(s)
print(f"First unique character '{unique_char}' at index {index}")


s = "loveleetcode"
index, unique_char = first_unique_char(s)
print(f"First unique character '{unique_char}' at index {index}")


s = "aabb"
index, unique_char = first_unique_char(s)
print(f"First unique character '{unique_char}' at index {index}")

