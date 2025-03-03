"""
✿ Task: Merge Two 2D Arrays by Summing Values

❖ Problem Statement: The goal is to merge two 2D arrays (array1 and array2) by summing the values of the second elements when the first elements are the same. The merged array should be sorted based on the first elements.

★ Steps:
    1.Input: 
        ❖ You start with two 2D arrays: 
            ● array1: The first 2D array to be merged. 
            ● array2: The second 2D array to be merged.

    2.Initialization: 
        ❖ Define a method mergeArrays within a class Solution. 
        ❖ Initialize variables to keep track of important information: 
            ● result: An empty list that will store the merged array. 
            ● i, j: Two indices to iterate through array1 and array2, respectively.

    3.Process: 
        ❖ Traverse both arrays simultaneously to merge them: 
            ● Use a while loop to iterate through array1 and array2 as long as there are elements in both arrays. 
            ● If the first elements of the current rows in both arrays are equal: 
                ※ Sum the second elements and append the result to the result list. 
                ※ Increment both indices i and j. 
            ● If the first element of the current row in array1 is smaller: 
                ※ Append the current row from array1 to the result list. 
                ※ Increment the index i. 
            ● If the first element of the current row in array2 is smaller: 
                ※ Append the current row from array2 to the result list. 
                ※ Increment the index j.

        ❖ After exiting the loop, append any remaining elements from array1 and array2 to the result list.

    4.Output: 
        ❖ Return the result list after merging the arrays.
"""



class Solution:
    def mergeArrays(self, array1, array2):
        result = []
        i, j = 0, 0

        while i < len(array1) and j < len(array2):
            if array1[i][0] == array2[j][0]:
                result.append([array1[i][0], array1[i][1] + array2[j][1]])
                i += 1
                j += 1
            elif array1[i][0] < array2[j][0]:
                result.append(array1[i])
                i += 1
            else:
                result.append(array2[j])
                j += 1

        result.extend(array1[i:])
        result.extend(array2[j:])

        return result

solution = Solution()
array1 = [[1, 2], [2, 3], [4, 5]]
array2 = [[1, 4], [3, 2], [4, 1]]
merged_array = solution.mergeArrays(array1, array2)
print(merged_array)





#=====================================================

