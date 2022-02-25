"""
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]

Examples

[1, 45, "Hi", False] ➞ [2, 1, 1, 0, 0, 0]


[[10, 20], ("t", "Ok"), 2, 3, 1] ➞ [3, 0, 0, 1, 1, 0]


["Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23] ➞ [2, 2, 3, 1, 0, 2]


[4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6] ]➞ [2, 0, 1, 2, 2, 0]

"""

veri = ["a", "b", True, (False,1), {1:"2"}, [1,2], {"2":"two"}, {2,"3"}, "c", 23, 0]
tip = ["int", "str", "bool", "list", "tuple", "dict"]
total = {}.fromkeys(tip, 0)
for i in range(len(veri)) :
    if type(veri[i]) == str :
        total["str"] += 1
    elif type(veri[i]) == bool :
        total["bool"] += 1
    elif type(veri[i]) == tuple :
        total["tuple"] += 1
    elif type(veri[i]) == list :
        total["list"] += 1
    elif type(veri[i]) == dict :
        total["dict"] += 1
    elif type(veri[i]) == int :
        total["int"] += 1
print(list( total.values()))