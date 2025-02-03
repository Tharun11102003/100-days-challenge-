"""
Task: Check if Array Is Sorted and Rotated

✿ Problem Statement: 
    ❖ Given a list of integers (numbers), determine if the list is sorted and rotated. A list is considered sorted and rotated if it is possible to rotate the list so that it becomes sorted in non-decreasing order. The list can only have at most one pair of consecutive elements that are out of order.

★ Steps:
    1.Input: 
        ❖ Provide a list of integers (numbers).

    2.Initialization: 
        ❖ Define a function check that takes the list numbers as an argument. 
        ❖ Initialize count to 0 to keep track of the number of out-of-order pairs. 
        ❖ Calculate the length of the list numbers.

    3.Process: 
        ❖ Iterate through the list elements from the second element to the last element. 
        ❖ For each element, compare it with the previous element. If the current element is smaller than the previous element, increment the count of out-of-order pairs. 
        ❖ After the loop, compare the last element of the list with the first element. If the last element is greater than the first element, increment the count again (this check handles the rotation case).

    4.Output: 
        ❖ Return True if the count of out-of-order pairs is less than or equal to 1, indicating the list can be sorted by a single rotation. Otherwise, return False.


"""

class Solution:
    def check(self, numbers):
        count, length = 0, len(numbers)
        for i in range(1, length):
            if numbers[i] < numbers[i - 1]:
                count += 1

        if numbers[length - 1] > numbers[0]:
            count += 1

        return count <= 1

solution = Solution()
numbers = [3, 4, 5, 1, 2]
print(solution.check(numbers))





#=======================================

