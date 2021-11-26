"""""

Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

The desired output is like :

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


"""

fibo = [1,1]
while fibo[-1] < 55 :
    fibo.append(fibo[-1]+ fibo[-2])
print(fibo)