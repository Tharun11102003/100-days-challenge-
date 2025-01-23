"""
Task: Map of Highest Peak

Problem Statement:
You are given a 2D grid, where each cell contains either a 1 (indicating water) or a 0 (indicating land). The goal is to determine the height of the highest peak for each cell in the grid. The height of a cell is defined by how far it is from the nearest water source, where water has a height of 0. You need to calculate the height of each land cell (0s) as the minimum number of steps required to reach a water source.

Steps:
    1.Input:
       ❖ A 2D grid called water_map, where each cell contains either 0 (land) or 1 (water).

    2.Process:
       ❖ Initialization:
           ● Create a height_map of the same dimensions as the water_map, initially filled with -1. This will represent the calculated height (distance) for each land cell.
           ● Water cells (cells with 1) will have their height set to 0 in the height_map.
           ● Create a queue to perform a breadth-first search (BFS), which will explore all cells starting from the water sources (cells with 1).

       ❖ BFS Execution:
           ● For each water cell, set its height to 0 and add it to the queue.
           ● Use BFS to explore neighboring cells. For each neighboring cell, if it hasn’t been visited yet (i.e., its value in height_map is -1), calculate its height (distance from the water) as the current cell’s height + 1, and add it to the queue for further exploration.
        
       ❖ Direction Handling:
           ● The BFS explores in four directions: down, up, right, and left. For each cell, the BFS checks if moving to a neighboring cell remains within grid boundaries, and if that cell hasn’t been visited yet.

    3.Output:
       ❖ After the BFS completes, the height_map will contain the minimum number of steps (height) to the nearest water source for each land cell.
"""


from collections import deque

water_map = [[0, 1], [0, 0]]
rows, cols = len(water_map), len(water_map[0])
height_map = [[-1] * cols for _ in range(rows)]
queue = deque()

for row in range(rows):
    for col in range(cols):
        if water_map[row][col]:
            height_map[row][col] = 0
            queue.append((row, col))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    current_row, current_col = queue.popleft()
    for d_row, d_col in directions:
        next_row, next_col = current_row + d_row, current_col + d_col
        if 0 <= next_row < rows and 0 <= next_col < cols and height_map[next_row][next_col] == -1:
            height_map[next_row][next_col] = height_map[current_row][current_col] + 1
            queue.append((next_row, next_col))

print(height_map)




#========================================
