"""
☞ Task: Temperature Converter
Problem Statement:
Create a program that converts temperatures between Celsius and Fahrenheit. The user should be able to input a temperature in one unit and get the converted temperature in the other unit.

☞ Steps to Solve the Problem:
Input:

※The user inputs the temperature value and the unit (Celsius or Fahrenheit).

●Process:

Convert the temperature to the other unit using the appropriate formula."""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    temp = float(input("Enter temperature value: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

    if unit == 'C':
        converted_temp = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        converted_temp = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

temperature_converter()
