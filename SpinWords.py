"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed . Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw"

spinWords("This is a test") => "This is a test"

spinWords("This is another test") => "This is rehtona test"

"""

def spinWords(string) :
    string = string.split()
    new_str = []
    for i in string :
        if len(i) <= 5 :
            new_str += [i]
        else :
            new_str += [i[::-1]]
    return " ".join(new_str)