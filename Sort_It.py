"""


In this challenge you will be given an array similar to the following:
[[3], 4, [2], [5], 1, 6]
In words, elements of the array are either an integer or an array containing a single integer. We humans can clearly see that this array can reasonably be sorted according to "the content of the elements" as:
[1, [2], [3], 4, [5], 6]
Create a function that, given an array similar to the above, sorts the array according to the "content of the elements".

Examples

sortIt([4, 1, 3]) ➞ [1, 3, 4]

sortIt([[4], [1], [3]]) ➞ [[1], [3], [4]]

sortIt([4, [1], 3]) ➞ [[1], 3, 4]

sortIt([[4], 1, [3]]) ➞ [1, [3], [4]]

sortIt([[3], 4, [2], [5], 1, 6]) ➞ [1, [2], [3], 4, [5], 6]

"""

def sortIt(arry) :
    n_arry = sorted([arry[i][0] if type(arry[i]) == list else arry[i] for i in range(len(arry))])
    return [[n_arry[i]] if n_arry[i] not in arry else n_arry[i] for i in range(len(arry))]
