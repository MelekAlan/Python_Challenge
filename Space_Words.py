"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example

"camelCasing"     =>  "camel Casing"

"identifier"      =>  "identifier"

""                =>  ""

"breakCamelCase"  => "break Camel Case"

"""

s = input("")
new_s = ""
for i in s :
    if i.isupper() :
        new_s += " " + i
    else:
        new_s += i
print(new_s)