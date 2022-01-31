"""

write a program to find all the Armstrong numbers present in between two intervals in Python. 
For example, Armstrong numbers between 100 and 2000. 
Expected output:
153
370
371
407
1634

"""


lower_num, higher_num = list(map(int, input("").split()))
for i in range(lower_num, higher_num+1) :
    if sum([int(j) ** len(str(i)) for j in str(i)]) == i :
        print(i)