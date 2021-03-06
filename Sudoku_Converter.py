"""

Objective:
To improve your control flow statement skills.
Task: The department you work for has received a project that displays the solved sudoku puzzles in a digital environment. 

Write a Python code to print out the given sudoku puzzle matrix in the following format.
Given format :
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
Desired output format :
- - - - - - - - - - - - - - - 
0  0  0  | 0  6  4  | 0  0  0  
7  0  0  | 0  0  0  | 3  9  0  
8  0  0  | 0  0  0  | 0  0  0  
- - - - - - - - - - - - - - - 
0  0  0  | 5  0  2  | 0  6  0  
0  8  0  | 4  0  0  | 0  0  0  
3  5  0  | 6  0  0  | 0  7  0  
- - - - - - - - - - - - - - - 
0  0  2  | 0  0  0  | 1  0  3  
0  0  1  | 0  5  9  | 0  0  0  
0  0  0  | 0  0  0  | 7  0  0  
- - - - - - - - - - - - - - -

Note that;

Use not more than "control flow statement and boolean logic operators" in solving this code problem.
The output which we expect from you is only a new output format above.
We don't expect a sudoku puzzle solver from you.

"""


new_sudoku = []
for i in range(len(sudoku)) :
    temp = []
    if i == 0 or i % 3 == 0 :
        new_sudoku += [[15 * "- "]]
    for j in range(len(sudoku[i])) :
        if j == 3 or j == 6 :
            temp.append("|")
            temp.append(sudoku[i][j])
            temp.append("")
        else :
            temp.append(sudoku[i][j])
            temp.append("")
    new_sudoku += [temp]
new_sudoku += [[15 * "- "]]

for i in new_sudoku :
    print(* i)