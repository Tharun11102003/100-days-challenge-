"""
Task: Removing Duplicates in a Sorted List
Problem Statement
You have a sorted list of integers and want to remove duplicates so that each element appears at most twice. The goal is to return the new length of the modified list.

Steps
    1.Input:
       ❖ A sorted list of integers, e.g., numbers = [1, 1, 1, 2, 2, 3].

    2.Process:
       ❖ Initialize:
           ● index to 1, which will keep track of the position to place the next unique element.

       ❖ Iterate through the list:
           ● Start from the second element (position 1) and check each element.
           ● If the current element is different from the element two positions before index or if index is 1 (to ensure the first two elements are not compared), then copy the current element to the index position and increment index.
    
       ❖ Condition check:
           ● The condition if index == 1 or numbers[i] != numbers[index - 2]: ensures that we either place the first two elements without comparison or place an element if it's not the same as the element two positions back.

    3.Output:
       ❖ The new length of the modified list, which is the value of index after the loop.
"""


numbers = [1, 1, 1, 2, 2, 3]
index = 1
for i in range(1, len(numbers)):
    if index == 1 or numbers[i] != numbers[index - 2]:
        numbers[index] = numbers[i]
        index += 1
print(index)




#================================================


