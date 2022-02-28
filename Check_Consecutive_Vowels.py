"""
In this coding challenge, you are going to write a program that takes a string and checks if it contains consecutive vowels or not. 
It should give Positive as an output if it contains consecutive vowels and Negative otherwise. 
For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels. 
So it should give Positive as an output. On the other hand, if you take the string of statoqag, the output should be Negative.

Expected Output:
Please enter a string: gasdph
Negative

Please enter a string: aiou
Positive

Please enter a string: taoum
Positive

Please enter a string: a
Negative

"""

vowels = list("aeiou")
string = input("Please enter a string: ")

new_vowels = "".join([i for i in string if i in vowels])

if all([ord(new_vowels[i]) - ord(new_vowels[i+1]) < 0 for i in range(len(new_vowels) -1)]) == True and len(new_vowels) > 1 :
    print("Positive")
else :
    print("Negative")


