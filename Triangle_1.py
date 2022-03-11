"""
      1 
     1 2 
    1 2 3 
   1 2 3 4 
  1 2 3 4 5

"""

num = int(input(""))
for i in range(1,num+1) :
    print(" " * (num +1 -i), *range(1,i+1))