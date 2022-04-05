"""
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers. 
If the input tries to divide by 0, return: "Can't divide by 0!"
"""

def calculator():
    num1 = float(input('Enter the first number > '))
    num2 = float(input('Enter the second number > '))
    operator = input('Enter the operator > ')
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        if num2 == 0:
            print("Can't divide by 0!")
        else:
            result = num1 / num2
    else:
        result = num1 * num2
    print(f'{num1} {operator} {num2} = {result}.')
    