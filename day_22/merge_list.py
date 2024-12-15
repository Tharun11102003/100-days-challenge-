"""
Task: Merge Two Sorted Lists
✿ Problem Statement: Write a Python function to merge two sorted lists into a single sorted list. The two input lists will be sorted in ascending order, and the resulting list should also be sorted in ascending order.

★ Steps:

1.Input: 
    ❖ The user provides two sorted lists of numbers.

2.Process: 
    ❖ Define a function merge_sorted_lists(list1, list2) that:
        ✥ Merges the Two Lists: - Concatenate both lists using the + operator.
        ✥ Sort the Combined List: - Use the sorted() function to sort the combined list in ascending order.
        ✥ Return the Sorted List: - Return the merged and sorted list.
"""



def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1_input = input("Enter the numbers for the first list, separated by spaces: ")
list1 = list(map(int, list1_input.split()))

list2_input = input("Enter the numbers for the second list, separated by spaces: ")
list2 = list(map(int, list2_input.split()))

merged_list = merge_sorted_lists(list1, list2)
print("The merged and sorted list is:", merged_list)
