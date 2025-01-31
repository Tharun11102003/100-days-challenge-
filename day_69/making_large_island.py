"""
Task: Making A Large Island
✿ Problem Statement: Given an n x n grid (matrix) of integers where each cell is either 0 (water) or 1 (land), you need to find the largest island that can be formed by changing at most one 0 to a 1.

★ Steps:
    1.Input:
       ❖ Provide the matrix: A 2D list of integers representing the grid.

    2.Initialization:
       ❖ Matrix size: 
           ● Determine the size of the matrix n.

       ❖ Visited matrix: 
           ● Create a visited matrix of the same size to track cells that have been processed.

       ❖ Component matrix: 
           ● Create a component matrix of the same size to assign component IDs to each connected component of 1s.

       ❖ Handle edge case: 
           ● If the matrix is of size 1, return 1 since changing the only 0 (if present) will result in an island of size 1.

    3.Process:
       ❖ Define the BFS function: 
           ● This function performs a breadth-first search to traverse and mark all cells in the current component, and returns the size of that component.

       ❖ BFS traversal: 
           ● For each unvisited land cell, start a BFS traversal to calculate the size of the connected component and assign component IDs. Store the sizes of the components.

       ❖ Calculate Largest Island:
           ● Check if all cells are 1s: If the entire matrix is already filled with 1s, return n*n as no change is needed.
        
       ❖ Iterate through water cells: 
           ● For each water cell (0), calculate the potential new island size by changing it to 1 and summing the sizes of the neighboring components.

       ❖ Track maximum area: 
           ● Keep track of the maximum island size possible by performing the change on each 0 cell.

    5.Output:
       ❖ Return the maximum island size: This is the largest possible island size after changing at most one 0 to 1.
"""


from typing import List
from collections import deque

class Solution:
    def largestIsland(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        visited = [[0] * n for _ in range(n)]
        component = [[0] * n for _ in range(n)]
        
        if n == 1:
            return 1

        def bfs(i, j, component_id):
            size = 0
            queue = deque([(i, j)])
            visited[i][j] = 1
        
            while queue:
                x, y = queue.popleft()
                component[x][y] = component_id
                size += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
            return size

        component_id = 1
        component_sizes = [-1] * (n * n)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1 and not visited[i][j]:
                    component_sizes[component_id] = bfs(i, j, component_id)
                    component_id += 1

        if all(matrix[i][j] == 1 for i in range(n) for j in range(n)):
            return n * n

        max_area = 1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    neighbors = set()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 1:
                            neighbors.add(component[ni][nj])
                    new_area = 1 + sum(component_sizes[comp_id] for comp_id in neighbors)
                    max_area = max(max_area, new_area)

        return max_area

grid = [[1, 0], [0, 1]]
solution = Solution()
print(solution.largestIsland(grid))





#=====================================

