"""
Task: Grid Game
Problem Statement:
You are given a 2xN grid where each cell contains an integer. The goal is to find the minimum possible value of the maximum sum of coins collected by two players moving from the top-left to the bottom-right of the grid.

Steps:
    1.Input:
       ❖ A 2D grid of integers, representing the values in each cell.

    2.Process:
       ❖ Initialization:
           ● Calculate the sum of all values in the top row and assign it to top_row_sum.
           ● Initialize bottom_row_sum to zero, representing the sum of values collected by Player 2.
           ● Initialize min_max_sum to infinity, representing the minimum possible maximum sum.

       ❖ Iterate through each column:
           ● Subtract the value in the current column of the top row from top_row_sum.
           ● Calculate the maximum of top_row_sum and bottom_row_sum, and update min_max_sum with the minimum value between the current min_max_sum and this calculated maximum.
           ● Add the value in the current column of the bottom row to bottom_row_sum.

    3.Output:
       ❖ The minimum possible value of the maximum sum of coins collected by the two players.
"""


class Solution:
    def game(grid):
        top_row_sum = sum(grid[0])
        bottom_row_sum = 0
        min_max_sum = float('inf')
        for i in range(len(grid[0])):
            top_row_sum -= grid[0][i]
            min_max_sum = min(min_max_sum, max(top_row_sum, bottom_row_sum))
            bottom_row_sum += grid[1][i]
        return min_max_sum

grid = [[2,5,4],[1,5,1]]
solution = Solution
ans = Solution.game(grid)
print(ans)



#============================