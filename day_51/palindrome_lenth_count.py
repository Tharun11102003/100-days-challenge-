"""
Task: Calculate Maximum Length of a Palindrome from Characters in a String

Problem Statement: You have a string consisting of lowercase alphabet characters. You want to calculate the maximum length of a palindrome that can be formed using the characters in the string.

Steps:
    1.Input:
       ❖ A string representing the characters available to form a palindrome.

    2.Process:
       ❖ Initialize Variables:
           ※ string = "abaacbcbb": The input string containing characters.
           ※ char_count = [0] * 26: An array to keep track of the frequency of each character in the string. The length is 26 to account for each letter in the English alphabet.
           ※ max_length = 0: A variable to store the calculated maximum length of the palindrome.

       ❖ Count Character Frequencies:
           ※ Iterate through each character in the input string.
           ※ For each character, update the corresponding position in char_count by incrementing its count. The position is determined by the difference between the character's ASCII value and the ASCII value of 'a'.

       ❖ Calculate Maximum Palindrome Length:
           ※ Iterate through the char_count array to check the frequency of each character.
           ※ If the frequency is zero, skip to the next character.
           ※ If the frequency is even, add the entire frequency to the max_length (as it can fully contribute to forming a palindrome).
           ※ If the frequency is odd, add the largest even number less than the frequency to the max_length (as only pairs of characters can be used in a palindrome). Then add 1 to account for the central character in the palindrome (if needed).

    3.Output:
       ❖ Print the calculated maximum length of the palindrome using the characters in the input string.
"""


string = "abaacbcbb"
char_count = [0] * 26
max_length = 0

for character in string:
    char_count[ord(character) - ord('a')] += 1

for count in char_count:
    if count == 0:
        continue
    if count % 2 == 0:
        max_length += 2
    else:
        max_length += 1

print(max_length)
