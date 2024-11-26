"""
☞ numbers: This variable represents the tuple of numbers you want to sum.
☞ sum_of_numbers: This variable accumulates the total sum of the numbers in the tuple.
☞ number: This represents each individual number in the tuple as you iterate through it.

"""


numbers = (1, 2, 3, 4, 5)
sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += number

print(sum_of_numbers)  # Output: 15
