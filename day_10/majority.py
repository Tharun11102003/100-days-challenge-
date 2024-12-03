"""
Find the Majority Element
"""
numbers = [1, 2, 3, 4, 2]
unique_elements = []
duplicates = []

for number in numbers:
    if number not in unique_elements and number not in duplicates:
        unique_elements.append(number)
    elif number not in duplicates:
        duplicates.append(number)

print(f"Unique elements: {unique_elements}")
print(f"Duplicates: {duplicates}")

