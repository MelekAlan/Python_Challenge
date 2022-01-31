"""

Write a python code that finds the largest number among the 5 numbers given by the user as input.

It is forbidden to use max() function.

Indicate which computational thinking concepts have you used.

Example for user inputs and respective outputs

Input            Output
------------     ------
1 2 3 4 5         5
67 85 19 39       85


"""

nums = list(map(int, input("Please enter 5 number with a space : ").split()))

print(sorted(nums)[-1])