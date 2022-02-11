"""

You are given three integers  i, j and k representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by  (i, j, k) on a 3D grid where the sum i + j + k of  is not equal to  n .

Sample Input

1
1
1
2

Sample Output 

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Print an array of the elements that do not sum to 2 .

"""

x, y, z, n = int(input("")), int(input("")), int(input("")), int(input(""))
ls = []
for i in range(x +1) :
    for j in range(y+ 1) :
        for k in range(z + 1) :
            if i + j + k != n :
                ls.append([i,j,k])
print(ls)