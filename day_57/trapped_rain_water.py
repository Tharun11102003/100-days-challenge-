"""
Task: Calculating the Amount of Trapped Rainwater in a Grid

Problem Statement: You are given a grid where each cell represents the height of terrain. The goal is to determine how much rainwater can be trapped after a rain.

Steps:
    1.Input:
       ❖ A 2D grid of integers, representing the height of each cell in a terrain.

    2.Process:
       ❖ Initialize:
           ● Define grid dimensions.
           ● Use a min-heap for boundary cells and initialize variables for total trapped rainwater and maximum water level.

       ❖ Heap-Based Search:
           ● Process boundary cells, update the maximum water level, and calculate trapped rainwater for each cell.

       ❖ Boundary Initialization:
           ● Add and mark boundary cells as visited.

    3.Output:
       ❖ The total amount of rainwater trapped in the grid.
"""

import heapq

heightMap = [
    [12,13,1,12],
    [13,4,13,12],
    [13,8,10,12],
    [12,13,12,12],
    [13,13,13,13]
]

dirs = (0, 1, 0, -1, 0)
m, n = len(heightMap), len(heightMap[0])
if m <= 2 or n <= 2:
    print(0)

boundary = []
for i in range(m):
    boundary.append((heightMap[i][0], i, 0))
    boundary.append((heightMap[i][-1], i, n-1))
    heightMap[i][0] = heightMap[i][-1] = -1

for j in range(1, n-1):
    boundary.append((heightMap[0][j], 0, j))
    boundary.append((heightMap[-1][j], m-1, j))
    heightMap[0][j] = heightMap[-1][j] = -1

heapq.heapify(boundary)
ans, trapped_rain = 0, 0

while boundary:
    h, i, j = heapq.heappop(boundary)
    trapped_rain = max(trapped_rain, h)

    for a in range(4):
        i0, j0 = i + dirs[a], j + dirs[a + 1]
        if i0 < 0 or i0 >= m or j0 < 0 or j0 >= n or heightMap[i0][j0] == -1:
            continue
        cur = heightMap[i0][j0]
        if cur < trapped_rain:
            ans += trapped_rain - cur
         
        heightMap[i0][j0] = -1
        heapq.heappush(boundary, (cur, i0, j0))

print(ans)




#==============================

