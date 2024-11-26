"""
☞  Function Definition: The cumulative_sum function takes a list of numbers as input.
☞  Initialization: An empty list cumulative is initialized to store the cumulative sums, and current_sum is initialized to 0.
☞  Iterate Through Numbers: The function iterates through each number in the list, adds it to current_sum, and appends the updated sum to the cumulative list.
☞  Return the Result: After the loop, the cumulative list is returned, containing the cumulative sums.
"""

def cumulative_sum(numbers):
    cumulative = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative.append(current_sum)
    return cumulative

# Example usage
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
output = cumulative_sum(numbers)
print(f"The cumulative sum list is: {output}")
