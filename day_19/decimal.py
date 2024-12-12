"""
Binary to Decimal Converte
"""


def binary_to_decimal(binary_str):
    decimal = 0
    binary_str = binary_str[::-1]  # Reverse the string to start from the least significant bit
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal += 2 ** i
    return decimal


binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print(f"The decimal equivalent of {binary_input} is {decimal_output}.")
