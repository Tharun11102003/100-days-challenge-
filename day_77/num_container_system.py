"""
Task Name: Design a Number Container System

Problem Statement: You need to design a system that can store and manage numbers at specific indices and efficiently retrieve the smallest index for a given number.

Steps:
    1.Input:
       ● A series of commands representing actions to be performed on the system. The commands include initializing the system, changing the number at a specific index, and finding the smallest index for a specific number.
       ● Corresponding inputs for each command.

    2.Initialization:
       ● Create a class NumberContainers to manage the system.
       ● Use a dictionary index_to_number to store the number associated with each index.
       ● Use a dictionary number_to_indices to maintain a heap of indices for each number.

    3.Methods:
       ● __init__(): Initializes the dictionaries.
       ● change(index: int, number: int) -> None: 
           ※ Updates the number at the given index.
           ※ If the index is already associated with a number, update the index-to-number mapping and the number-to-indices heap accordingly.

       ● find(number: int) -> int: 
           ※ Finds and returns the smallest index for the given number.
           ※ If the number is not found in the dictionary, return -1.
           ※ Remove any indices from the heap that no longer have the correct number, and return the smallest valid index if it exists.

    4.Processing Commands:
       ● Initialize the NumberContainers system.
       ● Iterate through the list of commands and their respective inputs, performing the required actions:
           ※ For the "NumberContainers" command, reinitialize the system.
           ※ For the "find" command, retrieve the smallest index for the given number.
           ※ For the "change" command, update the number at the specified index.

    5.Output:
       ● Generate a list of results, where each element corresponds to the output of the respective command. If the command does not produce an output, append None.
"""


import heapq

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}  
        self.number_to_indices = {}  
    
    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            prev_number = self.index_to_number[index]
            if prev_number == number:
                return

        self.index_to_number[index] = number
        
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            return -1
        
        while self.number_to_indices[number] and self.index_to_number[self.number_to_indices[number][0]] != number:
            heapq.heappop(self.number_to_indices[number])

        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1

commands = ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
inputs = [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

nc = NumberContainers()
output = []

for i, command in enumerate(commands):
    if command == "NumberContainers":
        nc = NumberContainers()
        output.append(None)
    elif command == "find":
        number = inputs[i][0]
        result = nc.find(number)
        output.append(result)
    elif command == "change":
        index = inputs[i][0]
        number = inputs[i][1]
        nc.change(index, number)
        output.append(None)

print(output)
