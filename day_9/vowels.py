"""
1. Write a python code to accept a string and count the number of vowels and consonants"""

def count_vowels_and_consonants(string):
    vowels = "aeiou"
    num_vowels = 0
    num_consonants = 0
    
    for char in string:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    
    return num_vowels, num_consonants

user_input = input("Enter a string: ").lower()
vowels_count, consonants_count = count_vowels_and_consonants(user_input)

print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")
