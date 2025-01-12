"""
Task: Convert Roman Numeral to Integer

Problem Statement: You want to convert a given Roman numeral string into its corresponding integer value.Some Roman numerals involve subtractive combinations, where a smaller numeral before a larger numeral indicates subtraction (e.g., IV represents 4, IX represents 9).

Steps:
    1.Input:
       ❖ A string representing a Roman numeral is provided as input.

    2.Process:
       ❖ Create a dictionary that maps Roman numeral characters to their corresponding integer values.
       ❖ Initialize a variable to store the final integer value of the Roman numeral.
       ❖ For each subtractive combination, adjust the logic to account for the correct value.
       ❖ Iterate through each character in the string, and add the corresponding integer value from the dictionary to the variable.

    3.Output:
       ❖ The function returns the integer value of the Roman numeral.
"""


class Solution:
    def roman(self, s):
        roman_letter = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += roman_letter[char]
        return number

solution_instance = Solution()
user_input = input("Enter the value: ").upper()
result = solution_instance.roman(user_input)
print(result)



#======================================
