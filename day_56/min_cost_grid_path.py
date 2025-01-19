"""
Task: Finding the Minimum Cost Path in a Grid

Problem Statement: You're given a grid where each cell represents a cost. The objective is to navigate from the bottom-right corner to the top-left corner with the least total cost.

Steps:
    1.Input:
       ❖ A 2D grid of integers, representing the cost of entering each cell.

    2.Process:
       ❖ Initialize:
           ● Define the grid's dimensions (number of rows and columns).
           ● Use a min-heap to track cells to visit, starting with the bottom-right corner.
           ● Maintain a variable for the minimum cost, initially set to -1.
           ● Create a set to track visited cells.

       ❖ Heap-Based Search:
           ● Continuously process the cell with the smallest cost from the heap.
           ● Skip cells that have already been visited.
           ● If the current cell is the top-left corner, update the minimum cost and stop.
           ● Calculate row and column indices of the current cell.
           ● Evaluate adjacent cells (up, down, left, right) and push valid moves to the heap with updated costs.
           ● Moving costs are based on the values in the grid.

    3.Output:
       ❖ The minimum cost to travel from the bottom-right to the top-left corner, once found.
"""

import heapq

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
rows, cols = len(grid), len(grid[0])
heap = [(0, rows*cols-1)]
min_cost = -1
visited_cells = set()
while heap:
    cost, cell = heapq.heappop(heap)
    if cell in visited_cells:
        continue
    visited_cells.add(cell)

    if cell == 0:
        min_cost = cost
        break

    row, col = cell // cols, cell % cols
    if row > 0 and cell - cols not in visited_cells:
        step_cost = 0 if grid[row-1][col] == 3 else 1
        heapq.heappush(heap, (cost + step_cost, cell - cols))
    if col > 0 and cell - 1 not in visited_cells:
        step_cost = 0 if grid[row][col-1] == 1 else 1
        heapq.heappush(heap, (cost + step_cost, cell - 1))
    if row < rows - 1 and cell + cols not in visited_cells:
        step_cost = 0 if grid[row+1][col] == 4 else 1
        heapq.heappush(heap, (cost + step_cost, cell + cols))
    if col < cols - 1 and cell + 1 not in visited_cells:
        step_cost = 0 if grid[row][col+1] == 2 else 1
        heapq.heappush(heap, (cost + step_cost, cell + 1))

print(min_cost)




#========================================


