"""
Task: First Completely Painted Row or Column
Problem Statement:
You have a matrix and a sequence of numbers. Each number in the sequence corresponds to a cell in the matrix. The goal is to identify the step at which a whole row or a whole column in the matrix is entirely painted. If no row or column is fully painted by the end of the sequence, the answer is -1.

Steps:
    1.Input:
       ❖ sequence: This is a list of numbers representing the order in which cells are painted.
       ❖ matrix: This is a 2D list (or grid) where each cell contains a unique number.

    2.Initialization:
       ❖ Determine the number of rows and columns in the matrix.
       ❖ Calculate the total number of elements in the matrix.
       ❖ Create lists to keep track of the row and column positions of each number in the matrix.

       ❖ Mapping Values to Positions:
           ● Go through each cell in the matrix and record which row and column it belongs to.

       ❖ Tracking Paints:
           ● Create counters to keep track of how many cells have been painted in each row and column.

       ❖ Painting Process:
           ● As you go through each number in the sequence:
           ● Increase the counter for the respective row and column of that number.
           ● Check if the entire row or column has been painted.
           ● If a row or column is fully painted, record the step at which this happens and stop the process.

    3.Output:
       ❖ Return the step number at which a row or column is fully painted.
       ❖ If no row or column is fully painted by the end of the sequence, return -1.
"""

class Solution:
    def painted_row_column(sequence, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        total_elements = rows * cols

        row_index = [-1] * (total_elements + 1)
        col_index = [-1] * (total_elements + 1)
        
        for row_num, row in enumerate(matrix):
            for col_num, val in enumerate(row):
                row_index[val] = row_num
                col_index[val] = col_num
            
        row_paints = [0] * rows
        col_paints = [0] * cols
        
        for step, element in enumerate(sequence):
            row_paints[row_index[element]] += 1
            col_paints[col_index[element]] += 1
            if row_paints[row_index[element]] == cols or col_paints[col_index[element]] == rows:
                return step
        return -1

sequence = [2, 8, 7, 4, 1, 3, 5, 6, 9]
matrix = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
solution = Solution
result = Solution.painted_row_column(sequence, matrix)
print(result)




#==================================