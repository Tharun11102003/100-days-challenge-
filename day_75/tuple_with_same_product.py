"""
Task: Tuple with Same Product
Problem Statement:
❖ Given a list of integers (numbers), find the number of tuples (a, b, c, d) such that:
    a * b = c * d
    (a, b) and (c, d) are distinct pairs
Each valid tuple is counted 8 times due to different ordering possibilities.

Steps:
    1. Input:
        ❖ Provide a list of integers (numbers).

    2. Initialization:
        ❖ Define a method tupleSameProduct within a class Solution.
        ❖ Create a dictionary (product_count) to track the occurrences of each product.
        ❖ Initialize a variable (result) to store the count of valid tuples.

    3. Process:
        ❖ Iterate through all unique pairs (numbers[i], numbers[j]):
            ● Compute their product.
            ● Check if this product already exists in product_count.
                ※ If yes, add the existing count to result (since all previous occurrences form new tuples).
                ※ Update the product_count by increasing the count for this product.

    4. Output:
        ❖ Return result * 8 to account for all valid tuple arrangements.
"""


class Solution:
    def tupleSameProduct(self, numbers):
        product_count = {}
        result, length = 0, len(numbers)

        for i in range(length):
            for j in range(i + 1, length):
                product = numbers[i] * numbers[j]
                result += product_count.get(product, 0)
                product_count[product] = product_count.get(product, 0) + 1

        return result * 8


solution = Solution()
nums = [2, 3, 4, 6] 
print(solution.tupleSameProduct(nums)) 
