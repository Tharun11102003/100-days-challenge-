"""
Task: Check if a Parentheses String is Balanced
Problem Statement:
You have a string containing parentheses ) and ( and a corresponding string indicating which characters are "locked". You need to determine if the string is balanced. A balanced string has matching pairs of opening and closing parentheses in the correct order.

Steps:
    1.Input:
       ❖ string: 
           ※ This is the input string of parentheses, for example, "))()))".
       ❖ lock_status: 
           ※ This indicates which characters are "locked" (cannot be changed). '0' means the character can be changed, '1' means it is locked in place, for example, "010100".

    2.Process:
       ❖ Check Length: 
           ※ If the length of the string is odd, it cannot be balanced, so immediately return False.

       ❖ First Pass (Left to Right):
           ※ Initialize a balance counter to 0.
           ※ Iterate over the characters and their lock statuses from left to right.
           ※ For each character:
               ● If the character is not locked or is an opening parenthesis (, increase the balance.
               ● If the character is a closing parenthesis ), decrease the balance.
               ● If the balance becomes negative, return False because there are more closing parentheses than opening ones up to that point.

       ❖ Second Pass (Right to Left):
           ※ Reinitialize the balance counter to 0.
           ※ Iterate over the characters and their lock statuses from right to left.
           ※ For each character:
               ● If the character is not locked or is a closing parenthesis ), increase the balance.
               ● If the character is an opening parenthesis (, decrease the balance.
               ● If the balance becomes negative, return False because there are more opening parentheses than closing ones up to that point.

       ❖ Final Check: 
           ※ If neither pass resulted in a negative balance, return True indicating the string is balanced.

    3.Output:
       ❖ The function returns True if the string is balanced and False otherwise.
"""


string = "))()))"
lock_status = "010100"

if len(string) % 2 != 0: 
    print(False)
balance = 0
for char, lock in zip(string, lock_status):
    if lock == '0' or char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
    if balance < 0:
        print(False)
balance = 0

for char, lock in zip(reversed(string), reversed(lock_status)):
    if lock == '0' or char == ')':
        balance += 1
    elif char == '(':
        balance -= 1
    if balance < 0:
        print(False)
print(True)




#=================================================