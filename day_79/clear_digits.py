"""
Task: Clear Digits

✿ Problem Statement: 
    ❖ You have a string containing both digits and characters. The goal is to remove the digits and return the remaining characters in the string. Whenever a digit is encountered, the last character in the stack (if any) should be removed.

★ Steps: 
    1. Input: 
        ❖ You start with a string that has both digits and characters.

    2.Initialization: 
        ❖ You'll define a method within a class. 
        ❖ You'll create an empty list to store the characters.

    3.Process: 
        ❖ As you iterate through each character in the string: 
            ● If the character is a digit, you check if there's any character already stored. If so, you remove the last character. 
            ● If the character is not a digit, you add it to your list.

    4.Output: 
        ❖ After processing all characters, you combine the characters in your list into a single string. 
        ❖ This string, which no longer includes the digits, is then returned.
"""

class Solution:
    def removeDigits(self, input_string):
        character_stack = []
        for char in input_string:
            if char.isdigit():
                if character_stack:
                    character_stack.pop()
            else:
                character_stack.append(char)
        return "".join(character_stack)

solution_instance = Solution()

input_string = "cb34"

output_string = solution_instance.removeDigits(input_string)

print("Output:", [output_string])





#===================================


