"""

Have the function StringChallenge(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
Examples
Input: "hello*3"
Output: Ifmmp*3
Input: "fun times!"
Output: gvO Ujnft!

"""

import string
lower = string.ascii_lowercase
vowel = "aeiou"
letter = input("")
new_s = "".join([lower[(lower.index(i) + 1) % len(lower)] if i in lower else i for i in letter])
print("".join([i.upper() if i in vowel else i for i in new_s]))
