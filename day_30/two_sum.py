"""
Task: Find Two Numbers That Add Up to a Target
✿ Problem Statement: Write a Python program that takes an array of integers and a target integer, and returns the two numbers in the array that add up to the target.

★ Steps:
    1. Input:
        ❖ The user provides a list of integers and a target integer.

    2. Process:
        ❖ Define a function two_sum(nums, target) that:

            ※ Initialize a Hashmap:
                ● Use a dictionary called num_to_index to store the indices of the numbers.

            ※ Iterate Through the Array:
                ● Use enumerate(nums) to get both the index i and the value num for each number in the list.

            ※ For each number in the list:
                ● Calculate the Complement:
                    ○ Calculate the complement as target - num.

            ※ Check for Complement:
                ● If the complement exists in the num_to_index dictionary, return the pair [complement, num].

            ※ Update the Hashmap:
                ● Store the index of the current number in the num_to_index dictionary.

            ※ Return the Result:
                ● If no solution is found, return None.

    3. Output:
        ❖ Display the pair of numbers that add up to the target, or None if no such pair exists.
"""




def two_sum(nums, target):

    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [complement, num]
        
        num_to_index[num] = i

    return None

nums = [2, 1, 11, 15, 7]
target = 9
print(two_sum(nums, target)) 

