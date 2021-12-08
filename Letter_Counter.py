"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;

1.takes a sentence from the user,
2.counts the number of each letter of the sentence,
3.collects the letters/chars as a key and the counted numbers as a value in a dictionary.

Sample inputs	                      Outputs

hippo runs to us!	                {'s': 2, 'r': 1, 't': 1, 'h': 1, 'n': 1,'i': 1, 'u': 2, 'o': 2, 'p': 2, ' ': 3, '!': 1}

"""

def counter(text) :
    dictt = {}
    for i in text :
        if i not in dictt :
            dictt[i] = 1
        else :
            dictt[i] += 1 
    return dictt

text = input("")
counter(text)
