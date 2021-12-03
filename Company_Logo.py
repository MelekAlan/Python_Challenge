"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
*Print the three most common characters along with their occurrence count.
*Sort in descending order of occurrence count.
*If the occurrence count is the same, sort the characters in alphabetical order.

Input Format
A single line of input containing the string .

Constraints
has at least  distinct characters

Sample Input
aabbbccde

Sample 
b 3
a 2
c 2

Explanation
Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
Note: The string  has at least  distinct characters.

"""

s = input("")
common = [[i, s.count(i)] for i in set(s)]
common.sort(key=lambda x : x[-1], reverse=True)
for i in common[:3] :
    print(* i)