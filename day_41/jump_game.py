"""
Task: Minimum Number of Jumps to Reach the End
    1.Input:
       ❖ Start with a list of non-negative integers, nums, where each integer represents the maximum number of steps you can jump forward from that position.

    2.Algorithm:
       ❖ Track the maximum distance that can be reached from the current position.
       ❖ Count the number of jumps made to reach the end of the list.
       ❖ Update the end position of the current jump to decide when to make a new jump.

    3.Steps in the Process:
        ❖ Initialize:
           ● Begin with the given list of non-negative integers.
           ● Set max_reach to 0, representing the farthest position that can be reached.
           ● Initialize jumps to 0, which counts the number of jumps made.
           ● Set end_of_current_jump to 0, which marks the end position of the current jump.

        ❖ Loop:
           ● For each position i in the list (excluding the last element):
               ⁕ Update max_reach to the farthest position that can be reached from i.
            
           ● If i reaches end_of_current_jump:
               ⁕ Update end_of_current_jump to max_reach.
               ⁕ Increment jumps by 1.

    4.Output:
       ❖ After iterating through the list, return the total number of jumps needed to reach the end.
"""


class Solution:
    def jump(self, nums):
        max_reach, jumps, end_of_current_jump = 0, 0, 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i == end_of_current_jump:
                end_of_current_jump = max_reach
                jumps += 1

       
        return jumps
    
nums = [2,3,1,1,4]
solution = Solution()
result = solution.jump(nums)
print(f"The minimum number of jumps is {result}")






#=========================================