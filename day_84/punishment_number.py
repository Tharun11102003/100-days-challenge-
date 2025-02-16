"""
Task: Find the Punishment Number of an Integer

✿ Problem Statement: ❖ Given an integer limit, the goal is to find the sum of the squares of all the numbers from a predefined list that are less than or equal to this limit.

★ Steps:
    1.Input: 
        ❖ You start with an integer limit: 
            ※ limit: The threshold value up to which numbers from the predefined list will be considered.
    
    2.Initialization: 
        ❖ Define a method calculatePunishment within a class Calculation. 
        ❖ Create a predefined list numbers containing specific integer values.
    
    3.Process: 
        ❖ Initialize a variable totalPunishment to accumulate the sum of the squares of the numbers. 
        ❖ Iterate through the numbers list: 
            ※ Check if each number is less than or equal to the limit. 
                ● If yes, add the square of the number to totalPunishment. 
                ● If no, break the loop.
    
    4.Output: 
        ❖ Return the value of totalPunishment, which represents the sum of the squares of the numbers from the list that are less than or equal to the given limit.
"""


class Calculation:
    def calculatePunishment(self, limit):
        numbers = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 
                   379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 
                   991, 999, 1000]
        
        totalPunishment = 0
        for number in numbers:
            if number <= limit:
                totalPunishment += number * number
            else:
                break
        return totalPunishment


solution = Calculation()
result = solution.calculatePunishment(10)
print(result)








#======================================


