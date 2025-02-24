"""
Task: Successful Pairs of Spells and Potions
Problem Statement: Given two lists of integers, spells and potions, and an integer success, determine how many potions each spell can be paired with such that the product of the spell and potion is at least success. Return the results as a list.

Implementation and Demonstration
    1.Define the class:
       ❖ Create the Solution class and the successfulPairs method that accepts spells, potions, and success as inputs.

    2.Modify Potion Values:
       ❖ Calculate the minimum potion strength needed for each potion to achieve the success criteria and store it back in the potions list.

    3.Sort Potions:
       ❖ Sort the potions list.

    4.Find Successful Pairs:
       ❖ For each spell, use binary search to find the number of successful potion pairs.
"""


from bisect import bisect_right

class Solution:
    def successfulPairs(self, spells, potions, success):
        for i in range(len(potions)):
            minimum_strength = success // potions[i]
            remainder = success % potions[i]
            potions[i] = minimum_strength
            if remainder:
                potions[i] += 1

        potions.sort()
        result = []

        for spell in spells:
            index = bisect_right(potions, spell)
            result.append(index)

        return result

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
solution = Solution()
print(solution.successfulPairs(spells, potions, success))





#========================================================


