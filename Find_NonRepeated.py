"""
A book store is trying to find the books that are only left 1 in the stock. They have the book list and they ask you to find the books. You are going to write a computer program that finds the non-repeated values in the list. Also indicate how you have used computational thinking concepts to find the solution.

Sample list for the test runs is as follows:

products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

Expected Output:

To Kill a Mockingbird
In Cold Blood
Wide Sargasso Sea
I Capture The Castle
"""

products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

def NonRepeated(arry) :
    for i in set(arry) :
        if arry.count(i) == 1 :
            print(i)

