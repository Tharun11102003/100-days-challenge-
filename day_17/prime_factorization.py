"""
Prime Factorization Tool
"""


def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

num = int(input("Enter a number to find its prime factors: "))
if num <= 1:
    print("Please enter a number greater than 1.")
else:
    factors = prime_factors(num)
    print(f"The prime factors of {num} are: {factors}")
