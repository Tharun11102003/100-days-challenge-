"""
Task: Merge Two Sorted Lists
Problem Statement: Merge two sorted lists, list1 and list2, into one sorted list where list1 has extra space at the end to hold elements from list2.

Steps:
    1.Input:
       ❖ Two sorted lists: list1 and list2.
       ❖ Number of actual elements in list1: count1.
       ❖ Number of elements in list2: count2.

    2.Process:
       ❖ Calculate the last index where elements will be placed in the merged list.

       ❖ Use a loop to compare the last elements of the non-zero part of list1 and list2:
           ※ If the current element in list1 is larger, place it at the last position of the merged list and move to the next element in list1.
           ※ Otherwise, place the current element in list2 at the last position of the merged list and move to the next element in list2.
        
       ❖ Continue this process until all elements of one list are placed.
       ❖ If there are remaining elements in list2, place them in the remaining positions of list1.

    3.Output:
       ❖ The merged and sorted list in list1
"""


list1 = [1, 2, 3, 0, 0, 0] 
count1 = 3  
list2 = [2, 5, 6] 
count2 = 3 

last_index = count1 + count2 - 1  

while count1 > 0 and count2 > 0:
    if list1[count1 - 1] > list2[count2 - 1]:
        list1[last_index] = list1[count1 - 1]
        count1 -= 1
    else:
        list1[last_index] = list2[count2 - 1]
        count2 -= 1
    last_index -= 1

while count2 > 0:
    list1[last_index] = list2[count2 - 1]
    count2 -= 1
    last_index -= 1
print(list1)






#+==============================

