"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

"""


def find_uniq(liste) :
    for i in liste :
        if liste.count(i) == 1 :
            return i