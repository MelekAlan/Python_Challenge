"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers
"""
num1 = int(input("please enter a number : "))
num2 = int(input("please enter a number : "))
if num1 > num2 :
    bolen = num2
else:
    bolen = num1
for i in range(1,bolen+1):
    if num1 % i == 0 and num2 % i == 0 :
        total = i

print(total)