"""
✿ Task: Length of Longest Fibonacci Subsequence

❖ Problem Statement: The goal is to find the length of the longest subsequence in a list of integers that forms a Fibonacci-like sequence. A Fibonacci-like sequence is a sequence where the sum of two preceding numbers equals the current number.

★ Steps: 
    1. Input: 
        ❖ You start with a list of integers: 
            ● sequence: The list of integers for which the longest Fibonacci-like subsequence needs to be determined.

    2.Initialization: 
        ❖ Define a method findLongestSubsequence within a class FibonacciSequence. 
        ❖ Initialize variables to keep track of important information: 
            ● element_set: A set containing all elements of the list for O(1) lookup. 
            ● max_length: This will store the length of the longest Fibonacci-like subsequence found. 
            ● length: This stores the total number of elements in the list.

    3.Process: 
        ❖ Iterate through each pair of elements in the list to start potential Fibonacci-like subsequences: 
            ● For each pair of elements (sequence[i] and sequence[j]), initialize the first two numbers of the potential subsequence. 
            ● Continue finding the next Fibonacci-like number by checking if the sum of the current pair exists in the set. 
            ● Update current_length each time a new Fibonacci-like number is found. 
            ● Update max_length to be the maximum value between the current max_length and current_length.

    3.Output: 
        ❖ After processing all pairs of elements, return the max_length, which represents the length of the longest Fibonacci-like subsequence in the list.
"""


class FibonacciSequence:
    def findLongestSubsequence(self, sequence):
        element_set = set(sequence)
        max_length = 0
        length = len(sequence)

        for i in range(length):
            for j in range(i + 1, length):
                previous = sequence[j]
                current = sequence[i] + sequence[j]
                curr_length = 2

                while current in element_set:
                    previous, current = current, current + previous
                    curr_length += 1
                    max_length = max(max_length, curr_length)

        return max_length

sequence = [1, 2, 3, 4, 5, 6, 7, 8]
solution = FibonacciSequence()
print(solution.findLongestSubsequence(sequence)) 





#=====================================================


