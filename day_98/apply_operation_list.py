"""
✿ Task: Apply Operations to a List

❖ Problem Statement: The goal is to apply a specific set of operations on a list of integers. The operations involve doubling the value of consecutive identical non-zero numbers and shifting all resulting non-zero numbers to the left, filling the remaining positions with zeros.

★ Steps:
    1.Input: 
        ❖ You start with a list of integers: 
            ● numbers: The list of integers to be processed.

    2.Initialization: 
        ❖ Define a method applyOperations within a class Solution. 
        ❖ Initialize variables to keep track of important information: 
            ● result: A list of the same length as numbers, initialized with zeros. 
            ● result_index: An index to track the position in the result list. 
            ● index: An index to iterate through the numbers list.

    3.Process: 
        ❖ Traverse the numbers list to apply the operations: 
            ● Use a while loop to iterate through the numbers list up to the second last element. 
            ● Check if the current element is non-zero. 
            ● If the current element is equal to the next element, double the value and store it in the result list. Increment the index by 1 to skip the next element. 
            ● If the current element is not equal to the next element, store the current element in the result list. 
            ● Increment the result_index to move to the next position in the result list. 
            ● Increment the index to move to the next position in the numbers list.

        ❖ After the loop, check if there is a remaining non-zero element in the numbers list and store it in the result list.

    4.Output: 
        ❖ Return the result list after applying the operations.
"""



class Solution:
    def applyOperations(self, numbers):
        result = [0] * len(numbers)
        result_index = 0
        index = 0

        while index < len(numbers) - 1:
            if numbers[index] != 0:
                if numbers[index] == numbers[index + 1]:
                    result[result_index] = numbers[index] * 2
                    index += 1  
                else:
                    result[result_index] = numbers[index]
                result_index += 1
            index += 1
        
        if index < len(numbers) and numbers[index] != 0:
            result[result_index] = numbers[index]

        return result

nums = [1, 2, 2, 1, 1, 0]
solution = Solution()
result = solution.applyOperations(nums)
print(result)





#===========================================

