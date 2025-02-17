"""
Task: Construct the Lexicographically Largest Valid Sequence

✿ Problem Statement: ❖ Given an integer num, the goal is to construct the lexicographically largest sequence consisting of numbers from 1 to num such that each number x (1 ≤ x ≤ num) appears exactly twice in the sequence, and the two occurrences of x are exactly x positions apart. If x = 1, it only needs to appear once.

★ Steps: 
    1. Input: 
        ❖ You start with an integer num: 
            ※ num: The largest number to be included in the sequence.

    2.Initialization: 
        ❖ Define a method constructDistancedSequence within a class Solution. 
        ❖ Create a list sequence with size 2 * num - 1, initialized with zeros. 
        ❖ Create a boolean list used_nums with size num + 1 to keep track of used numbers.

    3.Process: 
        ❖ Use a helper method backtrack to construct the sequence recursively: 
            ※ Start with the initial position pos set to 0. 
            ※ If the current position pos is already filled (i.e., not zero), move to the next position. 
            ※ If the position pos reaches the end of the list, return True indicating a valid sequence is constructed. 
            ※ For each number number from num to 1: ● If the number is already used (used_nums[number] is True), skip to the next number. 
                ● If the number is 1, place it at the current position and mark it as used. 
                ● If the current number number can be placed at the current position pos and pos + number: 
                    ◇ Place number at positions pos and pos + number. 
                    ◇ Mark number as used. 
                    ◇ Recursively call backtrack for the next position (pos + 1). 
                    ◇ If a valid sequence is found, return True. 
                    ◇ Otherwise, backtrack by resetting positions pos and pos + number to zero and marking number as unused. 
        ❖ If all numbers have been tried and no valid sequence is found, return False.

    4.  Output: 
        ❖ Return the constructed sequence that satisfies the conditions and is lexicographically largest.
"""


class Solution:
    def constructDistancedSequence(self, num):
        sequence = [0] * (2 * num - 1)
        used_nums = [False] * (num + 1)
        self.backtrack(sequence, used_nums, num, 0)
        return sequence

    def backtrack(self, sequence, used_nums, num, pos):
        while pos < len(sequence) and sequence[pos] != 0:
            pos += 1
        if pos == len(sequence):
            return True

        for number in range(num, 0, -1):
            if used_nums[number]:
                continue

            if number == 1:
                sequence[pos] = 1
                used_nums[1] = True
                if self.backtrack(sequence, used_nums, num, pos + 1):
                    return True
                sequence[pos] = 0
                used_nums[1] = False
            elif pos + number < len(sequence) and sequence[pos + number] == 0:
                sequence[pos] = number
                sequence[pos + number] = number
                used_nums[number] = True
                if self.backtrack(sequence, used_nums, num, pos + 1):
                    return True
                sequence[pos] = 0
                sequence[pos + number] = 0
                used_nums[number] = False

        return False

sol = Solution()
print(sol.constructDistancedSequence(3))




#===================================


