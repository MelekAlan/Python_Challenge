"""
A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. 
For example, assume the input plain text is the following: "abcdxyz" If the shift value, n, is 4, then the encrypted text would be the following: "efghbcd" 
You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. 
The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged. 
Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

"""


def caesarCipher(text, n) :
    letters = "abcdefghijklmnopqrstuvwxyz"
    return "".join([letters[(letters.index(i) + n) % len(letters)] if i.isalpha() else i for i in text])