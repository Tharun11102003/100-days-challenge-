"""
Task: Calculate the H-index.
Problem Statement: Given a list of integers representing the number of citations each paper received, calculate the H-index of a researcher. The H-index is defined as the maximum value h such that the researcher has published h papers that have each been cited at least h times.

Steps:
    1.Input:
       ❖ citations: A list of integers where each integer represents the number of citations a paper received.

    2.Process:
       ❖ Calculate the total number of papers (total_papers).
       ❖ Sort the list of citations in ascending order.
       ❖ Iterate through each citation value and its corresponding index.
           ※ For each citation, check if the difference between the total number of papers and the current index is less than or equal to the current citation value.
           ※ If the condition is met, return the difference as the H-index.
       ❖ If no such value is found, return 0.

    3.Output:
       ❖ The H-index of the researcher.
"""

class Solution:
    def h_index(citations):
        total_papers = len(citations)
        citations.sort()
        for index, citation in enumerate(citations):
            if total_papers - index <= citation:
                return total_papers - index
        return 0

citations = [3, 0, 6, 1, 5]
solution = Solution.h_index(citations)
print(solution)





#=====================================