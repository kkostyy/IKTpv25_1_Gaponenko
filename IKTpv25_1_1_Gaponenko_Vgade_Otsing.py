from math import *
import math 
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu k�lje pikkus => ')) 
S=a**2
print("Ruudu pindala", round(S, 1))
P=4*a
print("Ruudu �mberm��t", round(P, 1))
di=a*math.sqrt(2) 
print("Ruudu diagonaal", round(di,2))
print()
print("Ristk�liku karakteristikud")
b=float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c=float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S=b*c
print('Ristk�liku pindala', round(S, 1))
P=2*(b+c)
print("Ristk�liku �mberm��t", round(P, 1))
di=math.sqrt(b**2+c**2)
print("Ristk�liku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi l�bim��t", round(d, 1))
S=pi*r**2
print("Ringi pindala", round(S, 1))
C=2*pi*r
print("Ringjoone pikkus", round(C, 2))











