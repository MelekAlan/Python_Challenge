""""

You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

"""

num = int(input(""))
alpha = "abcdefghijklmnopqrstuvwxyz"[0:num]
for i in range(num-1, -num, -1):
    x = abs(i)
    line = alpha[num: x:-1] + alpha[x:num]
    print(x * "--", "-".join(line), x * "--")