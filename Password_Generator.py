"""
Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

Expected Output:
Please enter your full name: StephenClarkson
rto8807

Please enter your full name: BillJames
ils6032

Please enter your full name: MarkJackson
jkr7034

Please enter your full name: CarlSmith
iih7800

"""

import random
import string

while True :
    name = input("Please enter your full name : ").lower()
    if " " in list(name) :
        print("Please enter your name without any spaces!")
        continue  
    else :
        letter = [random.choice(name) for i in range(3)]
        digit = [random.choice(string.digits) for i in range(3)]  # digit = [str(random.randint(0,10)) for i in range(3)]
        print("".join(letter + digit))
        break
            
