"""
Task: Letter Tile Possibilities

✿ Problem Statement: ❖ Given a string tile_str consisting of alphabetic characters, the goal is to find the number of possible non-empty sequences that can be formed using the characters in the string. Each sequence should be unique.

★ Steps:
    1.Input: 
        ❖ You start with a string tile_str: 
            ※ tile_str: The string from which you will form sequences.

    2.Initialization: 
        ❖ Define a method numTilePossibilities within a class Solution. 
        ❖ Create an array char_count with size 26 to store the count of each character in the string. 
        ❖ Create an array factorial with size len(tile_str) + 1 to store the factorials.

    3.Process: 
        ❖ Calculate the factorials: 
            ※ Iterate from 1 to len(tile_str), calculating the factorial of each number and storing it in the factorial array. 
        ❖ Count the occurrences of each character in the string: 
            ※ Iterate through the characters of tile_str, and for each character, increment its corresponding count in char_count. 
        ❖ Use a dynamic programming approach to count permutations: 
            ※ Initialize an array perm_counts with size len(tile_str) + 1 to store the number of permutations of each length. 
            ※ Set perm_counts[0] to 1. 
            ※ Iterate through the char_count array. For each character count, update the perm_counts array by considering the addition of the character to existing permutations. 
        ❖ Sum the counts of all non-empty permutations: 
            ※ Iterate through perm_counts from 1 to len(tile_str) and calculate the total number of permutations.

    4.Output: 
        ❖ Return the sum of all non-empty permutations stored in perm_counts. This gives the total number of possible sequences that can be formed using the characters in tile_str.
"""


class Solution:
    def numTilePossibilities(self, tile_str):
        char_count = [0] * 26
        factorial = [1] * (len(tile_str) + 1)
        
        # Calculate the factorials
        for i in range(1, len(tile_str) + 1):
            factorial[i] = i * factorial[i - 1]
        
        for char in tile_str:
            char_count[ord(char) - ord('A')] += 1
        
        perm_counts = [0] * (len(tile_str) + 1)
        perm_counts[0] = 1
        
        for i in range(26):
            if char_count[i] > 0:
                temp = [0] * (len(tile_str) + 1)
                for j in range(len(tile_str) + 1):
                    if perm_counts[j] > 0:
                        for k in range(1, char_count[i] + 1):
                            total_length = j + k
                            temp[total_length] += perm_counts[j] * factorial[total_length] // (factorial[k] * factorial[j])
                
                for j in range(len(tile_str) + 1):
                    perm_counts[j] += temp[j]
        
        return sum(perm_counts[1:])
        

solution = Solution()
tiles = "AAB"
print(solution.numTilePossibilities(tiles)) 




#======================================================

