"""
Task: Lexicographically Smallest List by Swapping Elements

Problem Statement: Given an array of integers (numbers) and a threshold (threshold), the goal is to transform the array into its lexicographically smallest form by allowing swaps of elements where the absolute difference between the elements being swapped is less than or equal to the threshold.

Steps:
    1.Input:
       ❖ numbers: 
           ● A list of integers representing the array elements.
       ❖ threshold: 
           ● An integer representing the maximum allowed difference between elements to be swapped.

    2.Process:
       ❖ Initialization:
           ● Calculate the length of the numbers array and assign it to length.
           ● Initialize a variable grp to zero, representing the group index for elements that can be swapped.
           ● Create a list elements that stores pairs of elements and their original indices, sorted by the element values.
           ● Initialize an index_map list with zeros, where each index represents the group index of the corresponding element in the numbers array.
           ● Initialize a list subsets with a single pair representing the start and end indices of the current group.

       ❖ Grouping Elements:
           ● Iterate through the elements list in reverse order (excluding the last element).
           ● If the absolute difference between the current element and the next element is less than or equal to threshold, update the start index of the current group.
           ● Otherwise, create a new group for the current element and update the group index grp.

       ❖ Reordering Elements:
           ● Iterate through the numbers array.
           ● For each element, use the index_map to find the corresponding group and update the element to the lexicographically smallest element within that group.
           ● Increment the start index of the group in the subsets list.

    3.Output:
       ❖ The lexicographically smallest form of the numbers array after performing the allowed swaps.
"""


from typing import List

class Solution:
    def lexicographicallySmallestArray(self, numbers: List[int], threshold: int) -> List[int]:
        length, grp = len(numbers), 0
        elements = sorted([[numbers[i], i] for i in range(length)], key=lambda x: x[0])
        index_map = [0] * length
        subsets = [[length - 1, length - 1]]
        for i in range(length - 2, -1, -1):
            if elements[i + 1][0] - elements[i][0] <= threshold:
                subsets[-1][0] = i
            else:
                subsets.append([i, i])
                grp += 1
            index_map[elements[i][1]] = grp
        for i in range(length):
            key = index_map[i]
            numbers[i] = elements[subsets[key][0]][0]
            subsets[index_map[i]][0] += 1
        return numbers

numbers = [1, 5, 3, 9, 8]
threshold = 2
solution = Solution()
print(solution.lexicographicallySmallestArray(numbers, threshold))
