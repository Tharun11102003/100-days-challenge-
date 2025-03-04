"""
✿ Task: Partition Array According to Given Pivot

❖ Problem Statement: The task is to partition an array around a given pivot value. Elements less than the pivot should come first, followed by elements equal to the pivot, and then elements greater than the pivot.

★ Steps: 
    1.Input: 
        ❖ You start with: 
            ● numbers: A list of integers to be partitioned. 
            ● pivot_value: The integer pivot value.

    2.Initialization: 
        ❖ Define a method pivotArray within a class Solution. 
        ❖ Initialize variables to keep track of important information: 
            ● less_than_pivot: An empty list that will store elements less than the pivot. 
            ● greater_than_pivot: An empty list that will store elements greater than the pivot. 
            ● pivot_count: A counter to keep track of the number of elements equal to the pivot.

    3.Process: 
        ❖ Traverse the array numbers to partition it: 
            ● Use a for loop to iterate through each number in numbers. 
            ● If number is less than pivot_value: 
                ※ Append number to less_than_pivot. 
            ● If number is equal to pivot_value: 
                ※ Increment pivot_count by 1. 
            ● If number is greater than pivot_value: 
                ※ Append number to greater_than_pivot.

        ❖ After traversing the array, concatenate the lists: ● Concatenate less_than_pivot, [pivot_value] * pivot_count, and greater_than_pivot to form the final partitioned list.

    4.Output: 
        ❖ Return the partitioned list as the result.
"""

class Solution:
    def pivotArray(self, numbers, pivot_value):
        less_than_pivot, greater_than_pivot, pivot_count = [], [], 0

        for number in numbers:
            if number < pivot_value:
                less_than_pivot.append(number)
            elif number == pivot_value:
                pivot_count += 1
            else:
                greater_than_pivot.append(number)

        return less_than_pivot + [pivot_value] * pivot_count + greater_than_pivot

nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
solution = Solution()
result = solution.pivotArray(nums, pivot)
print(result)





#=======================================================


