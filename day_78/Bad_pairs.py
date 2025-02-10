"""
Task: Count Number of Bad Pairs

✿ Problem Statement: 
    ❖ Given a list of integers (numbers), determine the number of "bad pairs." A pair (i, j) is considered bad if i < j and numbers[i] - i ≠ numbers[j] - j. The goal is to find the count of such pairs in the list.

★ Steps:
    1.Input: 
        ❖ Provide a list of integers (numbers).

    2.Initialization: 
        ❖ Define a method countBadPairs within a class Solution. 
        ❖ Initialize variables: ● freq as an empty dictionary to store the frequency of keys. 
            ● good_pairs to 0, which will count the number of good pairs (where numbers[i] - i == numbers[j] - j).

    3.Process: 
        ❖ Iterate through the elements of the list using their index (for i, num in enumerate(numbers)): 
            ● Calculate the key as num - i. 
            ● Increment good_pairs by the frequency of the current key (if it exists). 
            ● Update the frequency of the key in the dictionary.

    4.Output: 
        ❖ Calculate the total number of pairs as (n * (n - 1)) // 2, where n is the length of the list. ❖ Return the difference between the total number of pairs and good_pairs to get the count of bad pairs.
"""


class Solution:
    def countBadPairs(self, numbers):
        freq = {}
        good_pairs = 0

        for i, num in enumerate(numbers):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(numbers)
        return (n * (n - 1)) // 2 - good_pairs

nums = [4, 1, 3, 3]
solution = Solution()
print(solution.countBadPairs(nums))





#==================================


