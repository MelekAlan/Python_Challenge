"""
Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

[1, 2, 4, 5, 6, 7, 8, 9]
[1, 2, 4, 5, 7, 8, 9]
[1, 2, 4, 5, 7, 8]
[1, 2, 5, 7, 8]
[1, 2, 5, 7]
[1, 2, 7]
[1, 7]
[1]
[]

"""

liste = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
indeks = 0
uzunluk = len(liste)
while len(liste) > 0 :
    indeks = (2 + indeks) % uzunluk
    liste.pop(indeks)
    print(liste)
    uzunluk -= 1