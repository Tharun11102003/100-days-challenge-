"""
Task Name: Count Servers that Communicate

Problem Statement: You have a grid where some cells contain servers (marked as 1) and others are empty (marked as 0). The objective is to determine how many servers can communicate with at least one other server. Two servers can communicate if they are in the same row or column.

Steps:
    1.Input:
        A 2D grid representing the server layout.

    2.Initialization:
        Calculate the number of rows and columns in the grid.
        Create lists to count the number of servers in each row and column.

    3.Counting Servers:
        Traverse through the grid to count the number of servers in each row and column.

    4.Tracking Communication:
        Traverse the grid again to determine the servers that can communicate based on row and column counts.

    5.Output:
        Return the count of servers that can communicate with at least one other server.
"""

class Solution:
    def server_communicate(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows 
        col_count = [0] * cols 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        communication_count = 0 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        communication_count += 1
        return communication_count

grid = [[1, 0], [1, 1]]
solution = Solution()
result = solution.server_communicate(grid)
print(result)





#=========================================