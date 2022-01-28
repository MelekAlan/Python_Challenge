"""
Given a string of size n, write functions to perform following operations on string.
Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n). 
For example given word: "Hippopotamus"  

result =
Left Rotation :  opotamusHipp
Right Rotation :  amusHippopot

"""

def rotation(word, num, rotate) :
    if rotate.lower() == "left" :
        return word[num:] + word[:num]
    elif rotate.lower() == "right" :
        return word[-num] + word[:len(word) - num]
