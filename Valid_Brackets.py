"""

Write a function that given a string containing just the characters (, ), {, }, [ and ], determines if the input string is valid or not by using following rules.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example for user inputs and respective outputs

Input           Output
------------    ------
"()"            True
"()[]{}"        True
"(]"            False
"([)]"          False
"{[]}"          True
""              True

"""

brackets = input("Please enter bracket : ")

while brackets != "" :
    if "()" or "{}" or "[]" in brackets :
        brackets = brackets.replace("()", "").replace("{}", "").replace("[]", "")
print(brackets == "")