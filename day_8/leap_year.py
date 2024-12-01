"""
Leap year check
"""

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("leap")
    else:
        print("no")

input_year = int(input("Enter a year: "))
result = check_leap_year(input_year)
