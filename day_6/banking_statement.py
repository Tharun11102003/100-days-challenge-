"""☞ Task :Simple Banking System

☞ Problem Statement:
Create a program that simulates basic banking operations like creating an account, depositing money, withdrawing money, and checking the balance.

✥ Steps to Solve the Problem:


● Setup:
     ※ Create Global Variables:
            ❖ Use global variables to store the account holder's name and balance.

     ※ Define Functions for Each Operation:
            ❖ Functions to create an account, deposit money, withdraw money, and check the balance.

● Input:
     ※ User Commands:
            ❖ The user inputs commands to perform different banking operations, such as create, deposit, withdraw, balance, and exit.

● Process:
     ※ Perform Banking Operations:
            ❖ Create Account: Function to initialize an account with an account holder’s name.
            ❖ Deposit: Function to add money to the account balance.
            ❖ Withdraw: Function to subtract money from the account balance if sufficient funds are available.
            ❖ Check Balance: Function to display the current account balance.

● Output:
     ※ Display Results:

            ❖ Output the result of each banking operation to the user, such as successful creation of an account, amount deposited, amount withdrawn, or current balance.
"""


current_balance = {"balance": 0}

def create_account():
    global current_balance
    account_holder = input("Enter account holder's name: ")
    current_balance["holder"] = account_holder
    print(f"Account created successfully for {account_holder}.")

def withdraw_amount(withdrawal_amount):
    global current_balance
    if current_balance["balance"] == 0:
        print("Insufficient balance")
    elif withdrawal_amount > current_balance["balance"]:
        print("Insufficient balance")
    else:
        current_balance["balance"] -= withdrawal_amount
        print(f"Withdrew: ₹{withdrawal_amount}")
        return current_balance

def deposit_amount(deposit_amount):
    global current_balance
    if deposit_amount > 0:
        current_balance["balance"] += deposit_amount
        print(f"Deposited: ₹{deposit_amount}")
    else:
        print("Invalid deposit amount")

def banking_system():
    while True:
        print("\nCommands: create, deposit, withdraw, balance, exit")
        user_choice = input("Enter your preference: ").strip().lower()

        if user_choice == "create":
            create_account()
        elif user_choice == "withdraw":
            amount_to_withdraw = int(input("Enter amount to withdraw: "))
            withdraw_amount(amount_to_withdraw)
        elif user_choice == "deposit":
            amount_to_deposit = int(input("Enter amount to deposit: "))
            deposit_amount(amount_to_deposit)
        elif user_choice == "balance":
            print(f"Current balance: ₹{current_balance['balance']}")
        elif user_choice == "exit":
            print("Exiting the banking system.")
            break
        else:
            print(f"Enter a valid option. '{user_choice}' is not a valid option.")


banking_system()






#============================================================