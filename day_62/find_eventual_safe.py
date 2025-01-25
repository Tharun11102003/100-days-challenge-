"""
Task Name: Find Eventual Safe States
Problem Statement: You have a directed graph represented as a list of lists. The objective is to find all nodes that are "eventually safe." A node is considered safe if it can only lead to terminal nodes (nodes that have no outgoing edges) through any path. In simpler terms, starting at a safe node, there's no way to reach a cycle in the graph.

Steps:
    1.Input:
        A directed graph where each element in the list represents the nodes a particular node can reach.

    2.Initialization:
        Determine the number of nodes in the graph.
        Create a list to store nodes that are eventually safe.
        Use a set to keep track of nodes visited during the Depth First Search (DFS).
    
        Create a list to remember the state of each node:
            0: unvisited
            1: safe
            -1: unsafe

    3.Depth First Search (DFS):
        For each node, perform DFS to check if it is safe:
            If a node is already marked as safe or has no outgoing edges, it's safe.
            If a node is marked as unsafe or is already being visited (indicating a cycle), it's unsafe.
            Mark the node as visited.
            Check all neighbors of the node recursively. If any neighbor is unsafe, mark the current node as unsafe.
            If all neighbors are safe, mark the current node as safe.

        Tracking Safe Nodes:
            Iterate through all nodes and use the DFS function to check their safety. If a node is safe, add it to the list of safe nodes.

    4.Output:
        Return the list of nodes that are eventually safe.
"""


from typing import List

class Solution:
    def eventualSafeNodes(self, graph_input: List[List[int]]) -> List[int]:
        num_nodes = len(graph_input)
        safe_nodes = []
        visited_nodes = set()
        memoization = [0] * num_nodes

        def dfs(node):
            if memoization[node] == 1 or len(graph_input[node]) == 0:
                return True
            elif memoization[node] == -1 or node in visited_nodes:
                return False
            
            visited_nodes.add(node)
            
            for neighbor in graph_input[node]:
                if not dfs(neighbor):
                    memoization[node] = -1
                    return False

            memoization[node] = 1
            return True
        
        for node in range(num_nodes):
            if dfs(node):
                safe_nodes.append(node)
        
        return safe_nodes


graph_input = [[1,2],[2,3],[5],[0],[5],[],[]]
solution = Solution()
print(solution.eventualSafeNodes(graph_input))



#=================================================

