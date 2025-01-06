"""
Task: Find the k-th Factor of n
✿ Problem Statement:
Write a Python program that finds the k-th factor of a given integer n. A factor of n is a positive integer that divides n without leaving a remainder.

★ Steps:
    1.Input:
       ❖ The user provides an integer n and an integer k.

    2.Process:
       ❖ Define a class Solution with a method kthFactor(n, k) that:
           ※ Initializes an empty list factors to store the factors of n.
           ※ Sets kth_factor to -1 as a default value indicating the k-th factor is not found.

           ※ Iterates through all integers i from 1 to n:
               ● For each i, checks if it is a factor of n (i.e., n % i == 0).
               ● If i is a factor, appends it to the factors list.

           ※ After collecting all factors:
               ● Checks if k is less than or equal to the length of the factors list.
               ● If true, assigns the k-th factor (0-based index k-1) to kth_factor.

           ※ Returns the list of factors and the k-th factor.

    3.Output:
       ❖ The method returns the list of factors and the k-th factor.
       ❖ The print statement displays: Factors list is [factors], the k-th factor is kth_factor.
"""



class Solution:
    def kthFactor(self, n, k):
        factors = [] 
        kth_factor = -1 
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        if k <= len(factors):
            kth_factor = factors[k - 1]

        return factors, kth_factor

n = 14
k = 3
factors, kth_factor = Solution().kthFactor(n, k) 
print(f"Factors list is {factors}, the {k}rd factor is {kth_factor}.")










#==========================================


