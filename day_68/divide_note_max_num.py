"""
Task: Divide Nodes Into the Maximum Number of Groups

✿ Problem Statement:
   ❖ Given an undirected graph with num_nodes nodes and a list of edges (connections), we need to divide the nodes into the maximum number of groups such that each group is bipartite (can be colored with two colors such that no two adjacent nodes have the same color).

★ Steps:
    1.Input: 
        ❖ Provide the number of nodes (num_nodes) and a list of edges (connections) representing the graph.

    2.Initialization: 
        ❖ Create an adjacency list (adjacency_list) to represent the graph. ❖ Initialize a colors list to store the color of each node. Each node is initially uncolored (0). ❖ Define helper functions is_bipartite and find_depth.

    3.Process:
       ❖ Building the Graph:
           ● Convert the list of edges into an adjacency list representation (adjacency_list).
       ❖ Checking Bipartiteness and Finding Depth:
           ● For each uncolored node, check if the component containing this node is bipartite using the is_bipartite function.        
           ● If it is not bipartite, return -1 because it is impossible to divide nodes as required.
           ● If it is bipartite, find the maximum depth of the bipartite component using the find_depth function.

    4.Calculate Maximum Groups:
       ❖ Sum the maximum depths of all bipartite components to find the total number of groups.

    5.Output: 
        ❖ Return the total number of groups if the graph can be divided as required. If any component is not bipartite, return -1.
"""


from collections import deque
from typing import List

class Solution:
    def magnificentSets(self, num_nodes: int, connections):

        def is_bipartite(node, color_val):
            colors[node] = color_val
            group.append(node)
            for neighbor in adjacency_list[node]:
                if (not colors[neighbor] and not is_bipartite(neighbor, -1 * color_val)) or colors[neighbor] == color_val:
                    return False
            return True

        def find_depth(start_node):
            visited = [0] * num_nodes
            queue, visited[start_node], max_depth = deque([start_node]), 1, 0
            while queue:
                for _ in range(len(queue)):
                    for neighbor in adjacency_list[queue.popleft()]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = 1
                max_depth += 1
            return max_depth

        adjacency_list = [[] for _ in range(num_nodes)]
        for node1, node2 in connections:
            adjacency_list[node1 - 1].append(node2 - 1)
            adjacency_list[node2 - 1].append(node1 - 1)

        total_sets, colors = 0, [0] * num_nodes
        for current_node in range(num_nodes):
            if not colors[current_node]:
                group = []
                if not is_bipartite(current_node, 1):
                    return -1
                total_sets += max(find_depth(node) for node in group)
        return total_sets


solution = Solution()
num_nodes = 6
connections = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
print(solution.magnificentSets(num_nodes, connections))
