"""
✿ Task Name: Maximum Number of Fish in a Grid

✿ Problem Statement: Write a Python function to find the maximum number of fish that can be caught in a connected path on a grid. Given a grid of integers where each integer represents the number of fish in a cell, the function should return the maximum number of fish that can be caught by starting from any cell and moving to adjacent cells in the grid.

★ Steps:
    1.Input:
       ❖ Provide the grid of integers representing the number of fish in each cell.

    2.Initialization:
       ❖ Define the possible directions for movement (right, left, down, and up).
       ❖ Determine the number of rows and columns in the grid.
       ❖ Initialize a variable to keep track of the maximum number of fish caught.

    3.Process:
       ❖ Define a depth-first search (DFS) helper function to explore each cell and its neighbors.
       ❖ If the current cell has no fish, return 0.
       ❖ Otherwise, add the number of fish in the current cell to the fish count and mark the cell as visited.
       ❖ For each direction, calculate the new row and new column positions.
       ❖ If the new position is within the grid bounds and the cell has fish, recursively call the DFS function to add the fish from the neighboring cells.
       ❖ Return the total fish count for the current cell.

    4.Main Loop:
       ❖ Iterate through each cell in the grid.
       ❖ If the cell has fish, call the DFS function to calculate the fish count for the connected path starting from that cell.
       ❖ Update the maximum fish count if the current fish count is higher.
    5.Output:
       ❖ Return the maximum fish count.
"""


from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        max_fish = 0

        def dfs(row: int, col: int, rows: int, cols: int) -> int:
            fish_count = 0
            
            if grid[row][col] == 0:
                return fish_count
            
            fish_count += grid[row][col]
            grid[row][col] = -1  # Mark as visited

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] > 0:
                        fish_count += dfs(new_row, new_col, rows, cols)
            
            return fish_count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                max_fish = max(max_fish, dfs(row, col, rows, cols))

        return max_fish

grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]

solution = Solution()
max_fish = solution.findMaxFish(grid)
print(max_fish)





#================================

