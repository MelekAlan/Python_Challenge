"""
Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

"""

num = int(input("Please enter a number : "))
if num <= 0 :
    print("Please do not enter negative number or '0'")
elif num == 2 :
    print("2 is a prime number")
else:
    for i in range(2,num) :
        if num % i == 0 :
            print("{} is not a prime number".format(num))
            break
    else :
        print("{} is a prime number".format(num))
