"""
✿ Task: Maximum Absolute Sum of Any Subarray

❖ Problem Statement: The goal is to find the maximum absolute sum of any subarray within the given list of integers. The absolute sum is the largest difference between the cumulative sum of any subarray.

★ Steps:
    1.Input: 
        ❖ You start with a list of integers: 
            ● numbers: The list of integers for which the maximum absolute sum of any subarray needs to be determined.

    2.Initialization: 
        ❖ Define a method max_absolute_sum within a class Solution. 
        ❖ Initialize three variables to keep track of the running sum, minimum running sum, and maximum running sum: 
            ● current_sum: This will store the cumulative sum as you iterate through the list. 
            ● minimum_sum: This will store the minimum cumulative sum encountered. 
            ● maximum_sum: This will store the maximum cumulative sum encountered.

    3.Process: 
        ❖ Iterate through each number in the list: 
            ● For each number, add it to the current cumulative sum (current_sum). 
            ● Update maximum_sum to be the maximum value between the current maximum_sum and current_sum. 
            ● Update minimum_sum to be the minimum value between the current minimum_sum and current_sum.

    4.Output: 
        ❖ After processing the entire list, return the absolute difference between the maximum_sum and minimum_sum, which represents the maximum absolute sum of any subarray.
"""


class Solution:
    def max_absolute_sum(self, numbers):
        current_sum, minimum_sum, maximum_sum = 0, 0, 0
        for number in numbers:
            current_sum += number
            maximum_sum = max(maximum_sum, current_sum)
            minimum_sum = min(minimum_sum, current_sum)
        return abs(maximum_sum - minimum_sum)

numbers = [1, -3, 2, 3, -4]
solution = Solution()
print(solution.max_absolute_sum(numbers))






#====================================

