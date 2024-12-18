"""
Task: Remove Duplicates from a List 
✿ Problem Statement:
Write a Python program to remove all duplicates from a given list of numbers. The program should take a list as input and return a new list with all duplicates removed.

★ Steps:
    1. Input:
        ❖ The user provides a list of numbers.

    2. Process:
        ❖ Define a function remove_duplicates(numbers) that:

        ✥ Initialize a Set:
            ※ Use a set to keep track of unique numbers.

        ✥ Iterate Through the List:
            ※ For each element in the list, add it to the set if it's not already present.

        ✥ Convert the Set Back to a List:
            ※ Convert the set back to a list to get the list of unique numbers.

        ✥ Return the New List:
            ※ Return the list of unique numbers.

    3. Output:
        ❖ Display the new list with all duplicates removed.
"""







def remove_duplicates(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers


input_list = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(input_list)
print("New List:", result)











#===========================================================