"""
Task: Construct Smallest Number From DI String

✿ Problem Statement: ❖ Given a pattern string consisting of the characters 'I' and 'D', the goal is to construct the lexicographically smallest number that follows the given pattern. 'I' means the next number is greater, and 'D' means the next number is smaller.

★ Steps:
    1.Input: 
        ❖ You start with a string pattern: 
            ※ pattern: The string representing the sequence of 'I' and 'D' that dictates the order of the smallest number.

    2.Initialization: 
        ❖ Define a method smallestNumber within a class Solution. 
        ❖ Create a variable pattern_length to store the length of the pattern. 
        ❖ Initialize an empty string smallest_number to store the resulting number. 
        ❖ Initialize an empty list number_stack to use as a stack for constructing the number.

    3.Process: 
        ❖ Iterate through the range of the length of the pattern plus one: 
            ※ For each index, push the current number (index + 1) onto the stack. 
        ❖ When an 'I' is encountered or the end of the pattern is reached: 
            ※ Pop all elements from the stack and append them to the smallest_number in the order they are popped (LIFO).

    4.Output: 
        ❖ Return the constructed smallest_number which follows the given pattern 'I' for increasing and 'D' for decreasing.
"""


class Solution:
    def smallestNumber(self, pattern):
        pattern_length = len(pattern)
        smallest_number = ""
        number_stack = []
        
        for index in range(pattern_length + 1):
            number_stack.append(index + 1)
            
            if index == pattern_length or pattern[index] == 'I':
                while number_stack:
                    smallest_number += str(number_stack.pop())
        
        return smallest_number

sol = Solution()
pattern = "IIIDIDDD"
print(sol.smallestNumber(pattern))



