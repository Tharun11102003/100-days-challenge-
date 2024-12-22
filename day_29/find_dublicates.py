"""
Task: Find All Duplicates in an Array
✿ Problem Statement: Write a Python program that takes an array of integers as input and returns all the integers that appear more than once.

★ Steps:
    1.Input: 
        ❖ The user provides a list of integers.

    2.Process: 
        ❖ Define a function find_duplicates(numbers) that:
            ※ Initialize Sets: ● Use two sets: seen to track numbers we have encountered, and duplicates to store numbers that appear more than once.
            ※ Iterate Through the List: ● For each number in the provided list: ◦ If the number is already in the seen set, add it to the duplicates set. ◦ Otherwise, add the number to the seen set.
            ※ Return the Result: ● Convert the duplicates set to a list and return it.

    3.Output: ❖ Display the list of duplicate numbers.
"""



def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return list(duplicates)

input_list = [4, 3, 2, 7, 8, 2, 3, 1, 3]

duplicates = find_duplicates(input_list)
print(duplicates)











#======================================






