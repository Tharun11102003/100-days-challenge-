"""
Task: Maximum Ascending Subarray Sum
✿ Problem Statement: ❖ Given a list of integers (numbers), determine the sum of the maximum ascending subarray. An ascending subarray is a subarray where each element is greater than the previous one. The goal is to find the subarray with the highest sum under these constraints.

★ Steps:
    1.Input: 
        ❖ Provide a list of integers (numbers).

    2.Initialization: 
        ❖ Define a method maxAscendingSum within a class Solution. 
        ❖ Initialize variables:
           ● current_sum to the first element of the list.
           ● maximum_sum to current_sum, which will store the highest sum encountered.

    3.Process: 
        ❖ Iterate through the elements of the list starting from the second element (for index in range(1, len(numbers))). 
        
        ❖ Compare the current element numbers[index] with the previous element numbers[index - 1]:
           ● If numbers[index] > numbers[index - 1], it means the subarray is still ascending:
               ※ Add numbers[index] to current_sum.
            
           ● Else, it means the ascending subarray is broken:
               ※ Reset current_sum to the current element numbers[index]. 
        
        ❖ Update maximum_sum to be the maximum of maximum_sum and current_sum.

    4.Output: 
        ❖ Return maximum_sum, which represents the sum of the maximum ascending subarray.
"""

class Solution:
    def maxAscendingSum(self, numbers):
        current_sum = numbers[0]
        maximum_sum = current_sum
        
        for index in range(1, len(numbers)):
            if numbers[index] > numbers[index - 1]: 
                current_sum += numbers[index] 
            else:
                current_sum = numbers[index] 
                
            maximum_sum = max(maximum_sum, current_sum) 
        
        return maximum_sum


solution = Solution()
numbers = [10, 20, 30, 5, 10, 50]
result = solution.maxAscendingSum(numbers)
print(result)





#======================================

