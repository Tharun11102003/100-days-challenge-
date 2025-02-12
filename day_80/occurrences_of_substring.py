"""
Task: Remove All Occurrences of a Substring

✿ Problem Statement: ❖ You have a string input_string and a substring. The goal is to remove all occurrences of the substring from the input_string.

★ Steps: 
    1. Input: 
        ❖ You start with two strings: 
            ※ input_string: The main string in which the removal will take place. 
            ※ substring: The substring that needs to be removed from the input_string.

    2.Initialization: 
        ❖ You'll define a method removeOccurrences within a class Solution.

    3.Process: 
        ❖ As you iterate through the main string: 
            ※ Finding the Substring: 
                ● Use the find method to locate the index of the substring in the input_string. 

            ※ Check for the Substring: 
                ● If the substring is not found (index == -1), break the loop. 

            ※ Removing the Substring: 
                ● If the substring is found, remove it by slicing the input_string from the start to the found index, and then from the end of the substring to the end of the input_string.

    4.Output: 
        ❖ After processing the entire input_string, return the modified string which no longer contains any occurrences of the substring
"""


class Solution:
    def removeOccurrences(self, input_string: str, substring: str) -> str:
        
        while True:
            index = input_string.find(substring)
            if index == -1:
                break
            input_string = input_string[:index] + input_string[index + len(substring):]
        return input_string

solution = Solution()
result = solution.removeOccurrences("daabcbaabcbc", "abc")
print(result) 




#====================================

