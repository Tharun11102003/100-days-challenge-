"""
Task: Maximum Employees to Be Invited to a Meeting
Problem Statement
You want to compute the maximum number of employees that can be invited to a meeting based on their favorite choices. Each employee has a favorite colleague they wish to invite. This creates a directed graph where each node points to one other node. The goal is to determine the largest number of employees that can be included in the meeting.

Steps
    1.Input:
       ❖ A list of integers is provided as input. Each integer represents the favorite colleague of the corresponding employee.

    2.Process:
       ❖ Graph Initialization:
           ● Create a directed graph from the favorite list.
           ● Initialize in-degrees for all nodes.

       ❖ Topological Sorting:
           ● Identify and process nodes with zero in-degrees using a queue.
           ● Update in-degrees and longest chain lengths while processing the queue.

       ❖ Pair Cycles:
           ● Identify and sum the lengths of all pair cycles.

       ❖ Cycle Detection:
           ● Use Depth First Search (DFS) to detect cycles in the graph.
           ● Calculate the maximum cycle length encountered during the DFS.

       ❖ Final Calculation:
           ● Determine the maximum number of employees that can be invited by taking the maximum of the sum of the pair cycle lengths and the maximum cycle length.

    3.Output:
       ❖ Print the maximum number of employees that can be invited to the meeting.
"""


from enum import Enum
import collections

class State(Enum):
    kInit = 0
    kVisiting = 1
    kVisited = 2

class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        num_people = len(favorite)
        total_chain_length = 0  
        graph = [[] for _ in range(num_people)]
        incoming_edges = [0] * num_people
        longest_chain = [1] * num_people
        for person, fav in enumerate(favorite):
            graph[person].append(fav)
            incoming_edges[fav] += 1

        queue = collections.deque([person for person, degree in enumerate(incoming_edges) if degree == 0])
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                incoming_edges[neighbor] -= 1
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)
                longest_chain[neighbor] = max(longest_chain[neighbor], 1 + longest_chain[current])

        for person in range(num_people):
            if favorite[favorite[person]] == person:
                total_chain_length += longest_chain[person] + longest_chain[favorite[person]]

        max_cycle_length = 0 
        parent = [-1] * num_people
        visited = set()
        states = [State.kInit] * num_people
        def findCycle(node: int) -> None:
            nonlocal max_cycle_length
            visited.add(node)
            states[node] = State.kVisiting
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    findCycle(neighbor)
                elif states[neighbor] == State.kVisiting:
                    current = node
                    cycle_length = 1
                    while current != neighbor:
                        current = parent[current]
                        cycle_length += 1
                    max_cycle_length = max(max_cycle_length, cycle_length)
            states[node] = State.kVisited
        for person in range(num_people):
            if person not in visited:
                findCycle(person)

        return max(total_chain_length // 2, max_cycle_length)


favorite = [3, 0, 1, 4, 1]
solution = Solution()
result = solution.maximumInvitations(favorite)
print(result)








#=====================================

