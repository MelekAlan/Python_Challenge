"""
Move Capital Letters to the Front

Create a function that moves all capital letters to the front of a word.

Examples

cap_to_front("hApPy") ➞ "APhpy"

cap_to_front("moveMENT") ➞ "MENTmove"

cap_to_front("shOrtCAKE") ➞ "OCAKEshrt"

"""

def cap_to_front(text) :
    new_text = ""
    for i in text :
        if i.isupper() :
            new_text += i
            text = text.replace(i,"")
    return new_text+text



