"""
You are given a list which may contain sublists. Your task is to find the depth of the deepest sublist.

[a] = 1 depth
[[a]] = 2 depth
[[[a]]] = 3 depth, etc
Examples
deepest([1, [2, 3], 4, [5, 6]]) ➞ 2

deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5
"""

def deepest_sublist(liste):
    new_list = []
    count = 0
    liste = str(liste)
    for i in liste:
        if i == '[':
            count += 1
        elif i == ']':
            count -= 1
        new_list.append(count)
    return max(new_list)