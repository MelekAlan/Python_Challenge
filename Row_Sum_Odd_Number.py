"""
Given the triangle of consecutive odd numbers:
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8

"""

#Solution 1

def sum_odd(n) :
    odd = sum([i for i in range(n)])
    return sum([(2 * odd + 1) + (2 * i) for i in range(n)])


#Solution 2

def sum_odd(n) :
    return n ** 3