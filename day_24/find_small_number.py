"""
Task: Find the Smallest Number in a List 
✿ Problem Statement:
    Write a Python program to find the smallest number in a given list of numbers. The program should take a list as input and return the smallest number in the list.

★ Steps:
    1. Input:
        ❖ The user provides a list of numbers.

    2. Process:
        ❖ Define a function find_smallest_number(numbers) that:
            ✥ Initialize the Smallest Number:
                ※ Start with the first element as the smallest number.

            ✥ Iterate Through the List:
                ※ For each element in the list, check if it is smaller than the current smallest number.

            ✥ Update the Smallest Number:
                ※ If a smaller number is found, update the smallest number.

            ✥ Return the Smallest Number:
                ※ Return the smallest number found in the list.

    3. Output:
        ❖ Display the smallest number in the list.
"""





def find_smallest_number(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


input_list = [3, 5, 7, 2, 8, 10, 1]
smallest_number = find_smallest_number(input_list)
print("Smallest Number:", smallest_number)


















#===============================================