"""
Task: Check if List is Special
✿ Problem Statement: ❖ Given a list of integers (numbers), determine if the list is special. A list is considered special if no two consecutive numbers have the same parity (even or odd).

★ Steps:
    1.Input: 
        ❖ Provide a list of integers (numbers).

    2.Initialization: 
        ❖ Define a function isArraySpecial that takes the list numbers as an argument. 
        ❖ Initialize a loop to iterate through the list elements up to the second-to-last element.

    3.Process: 
        ❖ For each pair of consecutive elements in the list, check if they have the same parity (i.e., both even or both odd). 
        ❖ If any pair has the same parity, return False indicating the list is not special. 
        ❖ If the loop completes without finding any such pair, return True indicating the list is special.

    4.Output: 
        ❖ Return True if the list is special, otherwise return False.
"""


class Solution:
    def isArraySpecial(self, numbers):
        for index in range(len(numbers) - 1):
            if numbers[index] % 2 == numbers[index + 1] % 2:
                return False
        return True

sol = Solution()
print(sol.isArraySpecial([2, 1, 4])) 





#===============================
