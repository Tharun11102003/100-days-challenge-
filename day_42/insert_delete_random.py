"""
Task: Insert, Delete, and Get a Random Element

Purpose:
    The RandomizedSet class is designed to manage a set of integers, allowing efficient insertion, deletion, and retrieval of random elements.

How It Works:
    1.Initialization:
       ❖ The class initializes two data structures:
           ● values: A list to store the elements.
           ● val_to_index: A dictionary to map each value to its index in the list.

    2.Insert Method:
       ❖ This method adds a value to the set if it's not already present.
       ❖ It checks if the value exists in the dictionary. If not, it appends the value to the list and updates the dictionary with the new index.
       ❖ It returns True if the value was added and False if it was already in the set.

    3.Remove Method:
       ❖ This method removes a value from the set if it exists.
       ❖ It checks if the value exists in the dictionary. If it does, it finds the index of the value and replaces it with the last element in the list.
       ❖ The dictionary is updated with the new index of the last element.
       ❖ The value is then removed from both the list and dictionary.
       ❖ It returns True if the value was removed and False if it was not in the set.

    4.GetRandom Method:
       ❖ This method returns a random element from the set.
       ❖ It uses Python's random.choice() function to pick a random element from the list.

    5.Outputs Explained:

       ❖ Insert (10):
           ● Adds 10 to the set.
           ● Output: True (indicating that 10 was successfully added).

       ❖ Remove (10):
           ● Removes 10 from the set.
           ● Output: True (indicating that 10 was successfully removed).

       ❖ GetRandom:
           ● Returns a random element from the set.
           ● Output: A random value from the set (could be any of the values currently in the set
"""



import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.val_to_index = {}

    def insert(self, val):
        if val in self.values:
            return False
        
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val):
        if val not in self.values:
            return False

        index = self.val_to_index[val]
        self.values[index] = self.values[-1]
        self.val_to_index[self.values[-1]] = index
        self.values.pop()
        del self.val_to_index[val]
        return True
        
    def getRandom(self):
        return random.choice(self.values)

obj = RandomizedSet()
print(obj.insert(10)) 
print(obj.insert(20))
print(obj.remove(10)) 
print(obj.insert(10)) 
print(obj.insert(30)) 
print(obj.insert(20))
print(obj.getRandom())





#=====================================