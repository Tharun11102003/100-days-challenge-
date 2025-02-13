"""
✿ Task: Max Sum of a Pair With Equal Sum of Digits

❖ Problem Statement: The goal is to find the maximum sum of any two numbers in the list such that the sum of the digits of both numbers is equal. If no such pair exists, return -1.

★ Steps:
    1.Input: 
        ❖ You start with a list of integers:
           ※ numbers: 
               ● The list of integers for which the maximum sum pair needs to be determined based on the equality of the sum of their digits.

    2.Initialization: 
        ❖ Define a method maximumSum within a class Solution. 
        ❖ Initialize an array max_digit_sum of size 82 (0-81) to store the maximum number found for each possible digit sum. 
        ❖ Set the initial value of max_sum to -1.

    3.Process: 
        ❖ Iterate through each number in the list:
           ※ Calculate the Digit Sum: 
                ● For each number, calculate the sum of its digits.

           ※ Check for Existing Maximum with Same Digit Sum: 
                ● If the calculated digit sum already has a corresponding maximum number in max_digit_sum, calculate the potential maximum sum and update max_sum if the new sum is larger.

           ※ Update the Maximum Number for Digit Sum: 
                ● Update the max_digit_sum array with the current number if it is larger than the existing maximum number for the same digit sum.

    4.Output: 
        ❖ After processing the entire list, return the value of max_sum which represents the maximum sum of any two numbers with equal digit sums. If no such pair exists, max_sum will remain -1
"""


class Solution:
    def maximumSum(self, nums):
        max_digit_sum = [0] * 82
        max_sum = -1
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            if max_digit_sum[digit_sum] != 0:
                max_sum = max(max_sum, num + max_digit_sum[digit_sum])
            max_digit_sum[digit_sum] = max(max_digit_sum[digit_sum], num)
        return max_sum

numbers = [18, 43, 36, 13, 7]
solution = Solution()
print(solution.maximumSum(numbers)) 



#=======================================

