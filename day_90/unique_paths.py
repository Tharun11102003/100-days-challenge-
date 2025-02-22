"""
Task: Find Unique Paths in a Grid

Problem Statement: Given the dimensions of a grid (rows and columns), you need to determine the number of unique paths from the top-left corner to the bottom-right corner. The movement is restricted to either right or down.

Steps:

1. Input:
   ❖ Two integers, rows (m) and columns (n), represent the dimensions of the grid.

2. Process:
   ❖ Initialize a 2D list (paths_matrix) with dimensions rows x columns, filled with zeros.
   ❖ Set all elements in the last column to 1, as there is only one way to reach the destination from any cell in the last column (by moving down).
   ❖ Set all elements in the last row to 1, as there is only one way to reach the destination from any cell in the last row (by moving right).
   ❖ Iterate through the grid from the second-to-last row and second-to-last column, and for each cell, update its value to be the sum of the values in the cell directly below and the cell directly to the right. This is because the number of ways to reach the destination from a cell is the sum of the ways from the cell to its right and the cell below it.

3. Output:
   ❖ The value in the top-left cell of the matrix (paths_matrix[0][0]) represents the total number of unique paths from the top-left corner to the bottom-right corner.
"""


class UniquePathsSolution:
    def unique_paths(self, rows, columns):
        paths_matrix = [[0] * columns for _ in range(rows)]
        
        for row in range(rows):
            paths_matrix[row][columns - 1] = 1
        for col in range(columns):
            paths_matrix[rows - 1][col] = 1
        
        for row in range(rows - 2, -1, -1):
            for col in range(columns - 2, -1, -1):
                paths_matrix[row][col] = paths_matrix[row + 1][col] + paths_matrix[row][col + 1]
        
        return paths_matrix[0][0]

solution = UniquePathsSolution()
print(solution.unique_paths(3, 7)) 




#========================================


