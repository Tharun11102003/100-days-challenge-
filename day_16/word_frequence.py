"""
Multiplication Table Generator
"""



def multiplication(number, range_end):
    # Loop through numbers from 1 to range_end
    for i in range(1, range_end + 1):
        # Print the multiplication result of 'number' and 'i'
        print(f"{number} x {i} = {number * i}")

# Prompt the user to enter the number for which the multiplication table will be generated
number = int(input("Enter the number for which the multiplication table is to be generated: "))
# Prompt the user to enter the range up to which the table should be displayed
range_end = int(input("Enter the range up to which the table should be displayed: "))
    
# Call the multiplication function with the provided inputs
multiplication(number, range_end)
