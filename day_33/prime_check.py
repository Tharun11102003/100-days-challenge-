"""
Task: Check If Numbers Within a Range Are Prime
✿ Problem Statement: Write a Python program that takes a range of positive integers (start and end) as input and determines all prime numbers within that range (inclusive).

★ Steps:
    1.Input: 
        ❖ The user provides two positive integers: the start and end of the range.

    2.Process: 
        ❖ Define a function to check if a single number is prime: 
            ※ Prime Check Function:-   
                ○ Check for Special Case: 
                    ● If the number is less than or equal to 1, return False as it is not a prime number. 
                ○ Iterate Through Possible Divisors: 
                    ● Check divisibility from 2 up to the square root of the number. If the number is divisible by any of these, return False.
                ○ Determine Primality: 
                    ● If no divisors are found, return True as the number is prime.

        ❖ Define a function to find all prime numbers within the specified range: 
            ※ Range Iteration: - 
                ○ Check Each Number in Range: 
                    ● For each number in the specified range, check if it is prime using the prime check function.
                ○ Collect and Display Primes: 
                    ● Store and print all prime numbers found in the range.

    3.Output: 
        ❖ Display a list of all prime numbers within the given range.
"""



def is_prime(number):
    if number <= 1: 
        return False
    for i in range(2, int(number**0.5) + 1): 
        if number % i == 0:
            return False
    return True  

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    start = int(input("Enter the start of the range: ")) 
    end = int(input("Enter the end of the range: ")) 

    if start > end:
        print("Invalid range. Start should be less than or equal to end.")
    else:
        primes = find_primes_in_range(start, end)
        print(f"Prime numbers between {start} and {end}: {primes}")

main()
