"""
Task: Counting Words With a Given Prefix

Problem Statement: You want to count how many words in a given list start with a specified prefix.

Steps:
    1.Input:
       ❖ A list of words is provided as input.
       ❖ A string representing the prefix you want to search for within the words.

    2.Process:
       ❖ Initialize a variable (count) to zero. This will keep track of the number of words that start with the specified prefix.
       ❖ Iterate through each word in the list.
       ❖ For each word, check if it starts with the specified prefix using the startswith method.
       ❖ If the word starts with the prefix, increment the count variable by one.

    3.Output:
       ❖ After iterating through all the words, the count variable will hold the number of words that start with the given prefix.
       ❖ The program then prints the value of the count variable
"""


word_list = ["pay","attention","practice","attend"]
prefix = "at"
count = 0
for word in word_list:
    if word.startswith(prefix):
        count += 1
print(count)








#=====================================