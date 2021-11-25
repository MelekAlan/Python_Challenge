"""
Task : Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
1. Collect all these numbers into a list
2. The desired output for n=100 :

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]

"""

def list_prime(n) :
    prime_num = []
    for i in range(2,n+1) :
        for j in range(2,i) :
            if i % j == 0 :
                break
        else :
            prime_num += [i]
    return prime_num