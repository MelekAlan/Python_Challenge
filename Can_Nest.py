"""
Check if One Array can be Nested in Another
Create a function that returns true if the first array can be nested inside the second.
arr1 can be nested inside arr2 if:
arr1's min is greater than arr2's min.
arr1's max is less than arr2's max.

Examples
canNest([1, 2, 3, 4], [0, 6]) ➞ True
canNest([3, 1], [4, 0]) ➞ True
canNest([9, 9, 8], [8, 9]) ➞ False
canNest([1, 2, 3, 4], [2, 3]) ➞ False
"""
def canNest(arry1,arry2) :
    return min(arry1) > min(arry2) and max(arry1) < max(arry2)
