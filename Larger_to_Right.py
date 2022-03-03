"""
Create a function that retrieves every number that is strictly larger than every number that follows it.
Examples

[3, 13, 11, 2, 1, 9, 5] ➞ [13, 11, 9, 5]

13 is larger than all numbers to its right, etc.

[5, 5, 5, 5, 5, 5] ➞ [5]

Must be strictly larger.

Always include the last number.

[5, 9, 8, 7] ➞ [9, 8, 7]

Notes

The last number in an array is trivially strictly larger than all numbers that follow it (no numbers follow it).

"""


arry = list(map(int, input("Please enter nums for list with a space : ").split()))

n_arry = []
for i in range(0, len(arry)-1):
    if all([arry[i] > j for j in arry[i+1:]]) :
        n_arry.append(arry[i])
print(n_arry + [arry[-1]])