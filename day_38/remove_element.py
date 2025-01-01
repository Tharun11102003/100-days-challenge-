"""
Task: Remove a Value from a List
Problem Statement: Write a Python function to remove all occurrences of a specific value from a list and return the new length of the modified list.

Steps:
    1.Input:
       ❖ Provide a list of integers nums and an integer val to the function.

    2.Algorithm:
       ❖ Use a loop to go through each element of the list.
       ❖ Maintain a counter to track the position for the next non-val element.

    3.Steps in the Function:
       ❖ Initialize:
           ● Start with a variable new_length set to 0. This variable will track the new length of the list without val.

       ❖ Loop:
           ● Use a for loop to go through each element in the list nums.
           ● If the current element is not val, place it in the position indicated by new_length.
           ● Increment new_length by 1 for each element that is not val.

       ❖ Return the New Length:
           ● After the loop finishes, return new_length, which represents the length of the list without the specified value val.

    4.Output:
       ❖ The function returns the new length of the modified list.
       ❖ The first new_length elements of the list nums are the ones that are not equal to val.
"""



class Solution:
    def removeElement(self, nums, val):
        new_length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_length] = nums[i]
                new_length += 1
        return new_length

nums = [3, 2, 2, 3]
val = 3

solution = Solution()
length = solution.removeElement(nums,val)

result = nums[:length]
print(result) 







#==================================