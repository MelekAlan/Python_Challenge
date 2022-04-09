"""
Given a string of size n, write functions to perform following operations on string.
Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n). For example given word: "Hippopotamus"  result =
Left Rotation :  opotamusHipp
Right Rotation :  amusHippopot
"""

def wise(text, n):
    c = 0
    res_1, res_2 = '', ''
    while c <= n - 1:
        res_1 += text[c]
        res_2 += text[::-1][c]
        c += 1
    left = text[n:] + res_1
    right = res_2[::-1] + text[:-n]
    return f'Left Rotation : {left}; Right Rotation : {right}'