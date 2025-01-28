"""
Task: Course Schedule IV

✿ Problem Statement: Write a Python function to determine if a course is a prerequisite for another course. Given the number of courses (numCourses), a list of prerequisites (prerequisites), and a list of queries (queries), the function should return a list of booleans. Each boolean indicates whether the first course in the query is a prerequisite for the second course.

★ Steps:

    Input: 
        ❖ Provide the number of courses (numCourses), a list of prerequisites (prerequisites), and a list of queries (queries).

    Initialization: 
        ❖ Create a mapping (course_to_prereqs) that associates each course with its list of prerequisites. 
        ❖ Use a defaultdict to store the mapping. 
        ❖ Create a memoization dictionary (memo) to store the results of previous checks for efficiency.

    Process: 
        ❖ Populate the mapping by iterating through the list of prerequisites. 
        ❖ Define a helper function (has_prerequisite) to perform a depth-first search (DFS) to check if one course is a prerequisite for another. 
        ❖ For each query, use the helper function to determine if the first course is a prerequisite for the second course. 
        ❖ Store the results of the queries in a list (result).

    Output: 
        ❖ Return the list of booleans (result), where each boolean corresponds to a query.
"""


from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course_to_prereqs = defaultdict(list) # course -> list of prerequisites

        for prereq in prerequisites:
            course_to_prereqs[prereq[1]].append(prereq[0])

        def has_prerequisite(course: int, required_course: int, memo: dict) -> bool:
            if (course, required_course) in memo:
                return memo[(course, required_course)]
            
            for prereq in course_to_prereqs[course]:
                if prereq == required_course or has_prerequisite(prereq, required_course, memo):
                    memo[(course, required_course)] = True
                    return True
            
            memo[(course, required_course)] = False
            return False
        
        memo = {}
        result = [has_prerequisite(query[1], query[0], memo) for query in queries]
        return result

numCourses = 2
prerequisites = [[1, 0]]
queries = [[0, 1], [1, 0]]
solution = Solution()
print(solution.checkIfPrerequisite(numCourses, prerequisites, queries))
