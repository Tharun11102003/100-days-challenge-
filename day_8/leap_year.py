"""
Leap year check
"""

def check_leap_year(year):
    if year % 4 == 0:
        print("leap")
    else:
        print("no")

input_year = int(input("Enter a year: "))
result = check_leap_year(input_year)
