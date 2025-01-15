"""
Task: Find the Prefix Common List of Two Lists

Problem Statement: You are given two lists of integers, list1 and list2, each containing the same number of elements. Your task is to count how many times each integer appears in both lists up to the current index and output the count at each step.

Steps:
    1.Input: 
        ❖ Two lists of integers representing the values to be counted:
           ● list1 = [1, 3, 2, 4]
           ● list2 = [3, 1, 2, 4]

    2.Process: 
        ❖ Initialize Variables:
           ● Determine the length of the lists.
           ● Initialize an empty list to store the results.
           ● Create a list to keep track of the occurrence of integers in both lists.
           ● Initialize a variable to count the repeated values.

        ❖ Iterate through the lists:
           ● For each index in the length of the lists, check the occurrence of the current element in list1 and list2.
           ● If an integer appears for the first time, mark it in the tracking list.
           ● If an integer has appeared before, increment the counter.
           ● Append the current value of the counter to the results list.

    3.Output: 
        ❖ Print the resulting list showing the count of repeated values at each step.
           ● Input:
               ⁕ list1 = [1, 3, 2, 4]
               ⁕ list2 = [3, 1, 2, 4]

           ● Output: 
               ⁕ [0, 2, 3, 4]
"""



list1 = [1, 3, 2, 4]
list2 = [3, 1, 2, 4]
length = len(list1)
results = []
flags = [0] * (length + 1)
counter = 0

for index in range(length):
    if flags[list1[index]] == 0:
        flags[list1[index]] = 1
    elif flags[list1[index]] == 1:
        counter += 1
    if flags[list2[index]] == 0:
        flags[list2[index]] = 1
    elif flags[list2[index]] == 1:
        counter += 1
    results.append(counter)

print(results)
