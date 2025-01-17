"""
Task: Bitwise XOR of All Pairing

Problem Statement: You want to compute the XOR of all elements in two lists based on specific conditions. If the length of one list is odd, you will XOR all elements in the other list. Finally, you print the result of XORing these two intermediate results.

Steps:
    1.Input:
        Two lists of integers are provided as input.

    2.Process:
        Compute the lengths of the two lists.
        Initialize two variables to store the results of XOR operations, both set to 0.

        Check if the length of the second list is odd:
            If yes, XOR all elements in the first list and store the result.

        Check if the length of the first list is odd:
            If yes, XOR all elements in the second list and store the result.
            Compute the final result by XORing the two intermediate results.

    3.Output:
        Print the final XOR result of the two intermediate results.
"""


list1 = [2,1,3]
list2 = [10,2,5,0]
length1 = len(list1)
length2 = len(list2)
xor_result1 = 0
xor_result2 = 0

if length2 % 2 != 0:
    for element in list1:
        xor_result1 ^= element
        
if length1 % 2 != 0:
    for element in list2:
        xor_result2 ^= element

print(xor_result1 ^ xor_result2)






#===============================================