"""
☞ Task : Build a BMI Calculator

☞ Problem Statement: Create a Python program that calculates the Body Mass Index (BMI) based on user input. The program should prompt the user to input their weight (in kilograms) and height (in meters), and then calculate and display their BMI along with the corresponding BMI category.

☞ Steps to Solve the Problem:
✥ Setup:
Define the Input:
    Prompt the user to input their weight and height.

✥ Input:
User Inputs:
    User inputs their weight (in kilograms) and height (in meters).

✥ Process:
Calculate the BMI:
    Use the formula BMI = weight / (height * height) to calculate the BMI.

Determine the BMI Category:
    Use conditional statements to determine the BMI category based on the calculated BMI.

✥ Output:
    Display the calculated BMI and the corresponding BMI category.
"""




def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    print(f"Your BMI is {bmi:.2f}.")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()






#===========================================