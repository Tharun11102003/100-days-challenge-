"""
Task: Check if One String Swap Can Make Strings Equal
✿ Problem Statement: ❖ Given two strings str1 and str2, determine if you can make the strings equal by swapping at most one pair of characters in one of the strings.

★ Steps:
    1.Input: 
        ❖ Provide two strings, str1 and str2.

    2.Initial Check: 
        ❖ If str1 and str2 are already equal, return True.

    3.Finding Differences: 
        ❖ Identify indices where the characters in str1 and str2 differ. ❖ Store these indices in a list called swap_indices.

    4.Checking Swap Possibility: 
        ❖ If there are exactly two indices in swap_indices:
           ● Let’s call them i and j.
           ● Check if swapping the characters at these indices in str1 would make the strings equal: ※ str1[i] should be equal to str2[j]. ※ str1[j] should be equal to str2[i].

    5.Output:
        ❖ Return True if a swap can make the strings equal, otherwise return False
"""


class Solution:
    def are_almost_equal(self, str1, str2):
        if str1 == str2:
            return True
        swap_indices = [i for i in range(len(str1)) if str1[i] != str2[i]]
        if len(swap_indices) == 2:
            i, j = swap_indices
            return str1[i] == str2[j] and str1[j] == str2[i]
        return False


s1 = "bank"
s2 = "kanb"
solution = Solution()
print(solution.are_almost_equal(s1, s2))  
