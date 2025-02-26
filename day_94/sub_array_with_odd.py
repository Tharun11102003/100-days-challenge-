"""
Task: Number of Sub-arrays With Odd Sum

Problem Statement: Given an array of integers, find the number of sub-arrays (contiguous sub-sequences) whose sum is odd. The function should return the number of such sub-arrays modulo  10^9 + 7.

Steps
    1.Input:
        ❖ An array of integers, e.g., [1, 3, 5].

    2.Process:
       ❖ Initialization:
            ● Define MODULO as 10^9 + 7 to handle large numbers.
            ● Initialize variables:
               ⁕ odd_sum_count to count sub-arrays with odd sums (initially 0).
               ⁕ even_sum_count to count sub-arrays with even sums (initially 1).
               ⁕ cumulative_sum to track the running sum of elements (initially 0).
               ⁕ result_count to accumulate the number of sub-arrays with odd sums (initially 0).

       ❖ Iteration:
            ● Traverse the array using a loop:
               ⁕ For each number in the array:
                    ※ Add number to cumulative_sum.
                    ※ Check if cumulative_sum is even or odd:
                       ⁜ If even:
                            ⊗ Add odd_sum_count to result_count and take modulo MODULO.
                            ⊗ Increment even_sum_count by 1.

                       ⁜ If odd:
                            ⊗ Add even_sum_count to result_count and take modulo MODULO.
                            ⊗ Increment odd_sum_count by 1.

    3.Output:
        ❖ The function returns result_count, representing the number of sub-arrays with odd sums modulo 10^9 + 7.
"""


class Solution:
    def numOfSubarrays(self, numbers_list):
        MODULO = 1000000007
        odd_sum_count, even_sum_count, cumulative_sum, result_count = 0, 1, 0, 0

        for number in numbers_list:
            cumulative_sum += number

            if cumulative_sum % 2 == 0:
                result_count = (result_count + odd_sum_count) % MODULO
                even_sum_count += 1
            else:
                result_count = (result_count + even_sum_count) % MODULO
                odd_sum_count += 1

        return result_count

arr = [1, 3, 5]
solution = Solution()
print(solution.numOfSubarrays(arr))  








#=====================================================================



