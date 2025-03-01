"""
✿ Task: Shortest Common Supersequence

❖ Problem Statement: The goal is to find the shortest common supersequence of two given sequences. A supersequence is a sequence that contains both given sequences as subsequences. The task is to merge both sequences while preserving their order and minimizing the length of the resulting supersequence.

★ Steps: 
    1.Input: 
        ❖ You start with two strings: 
            ● sequence1: The first string. 
            ● sequence2: The second string.

    2.Initialization: 
        ❖ Define a method shortestCommonSupersequence within a class Solution. 
        ❖ Initialize variables to keep track of important information: 
            ● length1, length2: Lengths of sequence1 and sequence2 respectively. 
            ● dp_table: A 2D list (table) to store the lengths of the longest common subsequence for substrings of sequence1 and sequence2.

    3.Process: 
        ❖ Create and fill the DP table: 
            ● Iterate through each character in both sequences. 
            ● If characters match, update the table by adding 1 to the value from the previous row and column. 
            ● If characters do not match, take the maximum value from the previous row or column.

        ❖ Build the shortest common supersequence: 
            ● Initialize two indices, idx1 and idx2, to the lengths of the sequences. 
            ● Traverse the DP table from the bottom-right to the top-left: 
            ● If characters match, add the character to the result list and move diagonally up-left. 
            ● If they do not match, move in the direction of the larger DP value. 
            ● Add any remaining characters from sequence1 or sequence2 to the result list. 
            ● Reverse the result list to get the final supersequence.

    4.Output: 
        ❖ After processing both sequences, return the resulting supersequence.
"""


class Solution:
    def shortestCommonSupersequence(self, sequence1, sequence2):
        length1, length2 = len(sequence1), len(sequence2)

        dp_table = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for idx1 in range(1, length1 + 1):
            for idx2 in range(1, length2 + 1):
                if sequence1[idx1 - 1] == sequence2[idx2 - 1]:
                    dp_table[idx1][idx2] = dp_table[idx1 - 1][idx2 - 1] + 1 
                else:
                    dp_table[idx1][idx2] = max(dp_table[idx1 - 1][idx2], dp_table[idx1][idx2 - 1])  # Take max from either previous row or column

        supersequence = []
        idx1, idx2 = length1, length2
        while idx1 > 0 and idx2 > 0:
            if sequence1[idx1 - 1] == sequence2[idx2 - 1]:
                supersequence.append(sequence1[idx1 - 1])
                idx1 -= 1
                idx2 -= 1
            elif dp_table[idx1 - 1][idx2] > dp_table[idx1][idx2 - 1]:  
                supersequence.append(sequence1[idx1 - 1])
                idx1 -= 1
            else:
                supersequence.append(sequence2[idx2 - 1])
                idx2 -= 1

        while idx1 > 0:
            supersequence.append(sequence1[idx1 - 1])
            idx1 -= 1

        while idx2 > 0:
            supersequence.append(sequence2[idx2 - 1])
            idx2 -= 1

        return ''.join(supersequence[::-1])

solution = Solution()
str1 = "abac"
str2 = "cab"
result = solution.shortestCommonSupersequence(str1, str2)
print(result)  




#========================================
