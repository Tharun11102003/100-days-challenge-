"""
Task: Redundant Connection

✿ Problem Statement: Write a Python function to find the redundant connection in a given list of edges in an undirected graph. Each edge in the list is a pair of nodes [u, v]. The graph should initially be a tree (connected and acyclic), and we need to find the edge that, if removed, will leave the graph as a tree.

★ Steps:
    1.Input: 
        ❖ Provide a list of edges (connections) representing an undirected graph.

    2.Initialization: 
        ❖ Create a list (parent) to store the parent of each node. Initialize this list such that each node is its own parent. 
        ❖ Define a helper function (find_parent) to find the root parent of a node using path compression.

    3.Process: 
        ❖ Iterate through each edge in the list of connections. 
        ❖ For each edge [node1, node2], find the root parents of both nodes (parent1 and parent2) using the find_parent function. 
        ❖ If both nodes share the same root parent (parent1 == parent2), it means adding this edge would create a cycle. Hence, return this edge as the redundant connection. 
        ❖ If the nodes do not share the same root parent, unify them by setting the parent of one node to be the parent of the other (parent[parent2] = parent1).

    4.Output: 
        ❖ Return the edge that forms the redundant connection, causing a cycle in the graph.
"""


from typing import List

class Solution:
    def findRedundantConnection(self, connections):
        parent = list(range(len(connections) + 1)) 

        def find_parent(node):
            if parent[node] != node:
                parent[node] = find_parent(parent[node]) 
            return parent[node] 

        for node1, node2 in connections: 
            parent1, parent2 = find_parent(node1), find_parent(node2)

            if parent1 == parent2:
                return [node1, node2] 
 
            parent[parent2] = parent1 

sol = Solution()
edges = [[1,2],[1,3],[2,3]]
print(sol.findRedundantConnection(edges))



#=======================================================