"""
Armstrong Number Checke"""


original_number = 371
current_number = original_number
total_sum = 0

number_of_digits = len(str(current_number))

for _ in range(number_of_digits):

    digit = int(current_number % 10)
    current_number = current_number // 10
    total_sum += pow(digit, number_of_digits)

if total_sum == original_number:
    print("Armstrong")
else:
    print("Not Armstrong")
