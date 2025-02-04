"""
Task: Find the Length of the Longest Strictly Increasing or Strictly Decreasing Subarray

✿ Problem Statement: ❖ Given a list of integers (arr), determine the length of the longest subarray that is either entirely strictly increasing or strictly decreasing. The sequence should strictly adhere to an increasing or decreasing pattern without allowing any equal elements.

★ Steps:
    1.Input: 
        ❖ Provide a list of integers (arr).

    2.Initialization: 
        ❖ Define a function longestStrictMonotonicSubarray. 
        ❖ Initialize variables: 
            ※ n to the length of arr. 
            ※ ans to 0, which will store the final answer. 
            ※ inc to 1, which will keep track of the length of the current strictly increasing subarray. 
            ※ dec to 1, which will keep track of the length of the current strictly decreasing subarray. 
        ❖ If the list has only one element, return 1 since the longest subarray length is 1.

    3.Process: 
        ❖ Iterate through the elements of the list starting from the second element (for i in range(1, n)). 
        ❖ Compare the current element arr[i] with the previous element arr[i-1]: 
            ● If arr[i] >arr[i-1], it means the subarray is strictly increasing: 
                ※ Incrementincby 1. 
                ※ Resetdecto 1 because the strictly decreasing sequence is broken. 

            ● Ifarr[i] < arr[i-1], it means the subarray is strictly decreasing: 
                ※ Incrementdecby 1. 
                ※ Resetincto 1 because the strictly increasing sequence is broken. 
                ※ Ifarr[i] == arr[i-1], bothincanddecare reset to 1 because the sequence must be strictly increasing or decreasing. 
        
        ❖ Update the answeransto be the maximum ofans,inc, anddec`.

    4.Output: 
        ❖ Return ans, which represents the length of the longest strictly monotonic subarray.
"""


class Solution:
    def longestMonotonicSubarray(self, arr):
        n, ans, inc, dec = len(arr), 0, 1, 1
        if n == 1: return 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                inc += 1
                dec = 1
            elif arr[i] < arr[i-1]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            ans = max(ans, dec, inc)
        return ans


nums = [3, 3, 3, 3]
solution = Solution()
print(solution.longestMonotonicSubarray(nums)) 



#==========================================

