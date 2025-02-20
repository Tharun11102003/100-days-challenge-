"""
✿ Task: The k-th Lexicographical String of All Happy Strings of Length n

❖ Problem Statement: Given two integers length and position, the goal is to construct the k-th lexicographical string of all happy strings of length n. A happy string is a string that consists only of the characters 'a', 'b', and 'c' and does not contain any two consecutive characters that are the same.

★ Steps:
    1.Input: 
        ❖ You start with two integers: 
            ※ length: The desired length of the happy string. 
            ※ position: The k-th position of the lexicographical happy string.

    2.Initialization: 
        ❖ Define a method getHappyString within a class Solution. 
        ❖ Create a variable total_length to store the length of the happy string. 
        ❖ Define a recursive helper function dfs (depth-first search) to generate the happy string.

    3.Process: 
        ❖ The dfs function takes three parameters: prefix, remaining_length, and remaining_position. 
        ❖ Base Case: If remaining_length is 0, return the prefix. 
        ❖ Iterate through the characters 'a', 'b', and 'c': 
            ※ Check if the current character is the same as the last character in prefix; if so, skip it to ensure no two consecutive characters are the same. 
            ※ Calculate the count of happy strings that can be formed with the current prefix using 2 ** (total_length - len(prefix) - 1). 
            ※ If the count is greater than or equal to remaining_position, call the dfs function recursively with the updated prefix, reduced length, and position. 
            ※ Otherwise, subtract the count from remaining_position and continue to the next character. 
        ❖ If the function completes without finding the k-th happy string, return an empty string.

    4.Output: 
        ❖ Call the dfs function with an empty prefix, the given length, and position to generate the k-th lexicographical happy string. ❖ Return the generated happy string.
"""


class Solution:
    def getHappyString(self, length, position):
        def dfs(prefix, remaining_length, remaining_position):
            if remaining_length == 0:
                return prefix
            for character in 'abc':
                if prefix and character == prefix[-1]:
                    continue
                count = 2 ** (total_length - len(prefix) - 1)
                if count >= remaining_position:
                    return dfs(prefix + character, remaining_length - 1, remaining_position)
                else:
                    remaining_position -= count
            return ""
        
        total_length = length
        return dfs("", length, position)


solution = Solution()
print(solution.getHappyString(1, 3)) 




#==============================