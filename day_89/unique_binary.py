"""
Task: Find Unique Binary String
Problem Statement: You need to create a new binary string that is different from the given list of binary strings. The difference is achieved by flipping the binary digit at each index position where the index matches the value.

Steps:
    1.Input:
       ❖ A list of binary strings is provided as input.

    2.Process:
       ❖ Initialize an empty list to store the result.
       ❖ Iterate through the binary strings using their indices.
       ❖ For each binary string, check the binary digit at the current index:
           ※ If the binary digit is '0', append '1' to the result list.
           ※ If the binary digit is '1', append '0' to the result list.
       ❖ After processing all binary strings, join the elements of the result list to form the final result.

    3.Output:
       ❖ The new binary string that differs from the provided list is generated.
"""


class Solution:
    def findDifferentBinaryString(self, binary_strings):
        diff_binary_string = []
        for index in range(len(binary_strings)):
            if binary_strings[index][index] == '0':
                diff_binary_string.append('1')
            else:
                diff_binary_string.append('0')
        return ''.join(diff_binary_string)

nums = ["01", "10"]
solution = Solution()
print(solution.findDifferentBinaryString(nums))





#================================

