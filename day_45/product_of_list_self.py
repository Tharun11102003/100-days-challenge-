"""
Task: Product of list except the self.
Problem Statement:
Given a list of integers, nums, return a list, res, such that res[i] is the product of all the elements of nums except nums[i].

Steps:
1. Input: 
    ❖ A list of integers, nums.

2. Process: 
    ❖ Calculate the length of the input list, n. 
    ❖ Initialize a result list, res, with all elements as 1. 
    ❖ Initialize a variable, left, to keep track of the product of elements to the left of the current position.

    ❖ Use a loop to iterate through the list from left to right: 
        ※ Set the current element of res to left. 
        ※ Update the left product by multiplying it with the current element of nums.

    ❖ Initialize a variable, right, to keep track of the product of elements to the right of the current position.

    ❖ Use a loop to iterate through the list from right to left: 
        ※ Multiply the current element of res with the right product. 
        ※ Update the right product by multiplying it with the current element of nums.

3. Output: 
    ❖ The resulting list, res, which contains the product of all elements in nums except the element at the current position.
"""


def product_except_self(nums):
    n = len(nums)
    res = [1] * n 
    left = 1  
    for i in range(n):
        res[i] = left
        left *= nums[i]  
    right = 1 #24
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    
    return res

nums1 = [1, 2, 3, 4]

print(product_except_self(nums1))  




#============================================
