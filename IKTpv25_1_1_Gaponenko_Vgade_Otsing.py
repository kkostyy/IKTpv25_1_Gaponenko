from math import *

print("Ruudu karakteristikud")
a = float(input("Sisesta ruudu k�lje pikkus => "))  # Added input()
S = a**2
print("Ruudu pindala", round(S, 1))
P = 4 * a
print("Ruudu �mberm��t", round(P, 1))  
di = a * sqrt(2)  # Removed math. since we used from math import *
print("Ruudu diagonaal", round(di, 2))
print()

print("Ristk�liku karakteristikud") 
b = float(input("Sisesta ristk�liku 1. k�lje pikkus => "))
c = float(input("Sisesta ristk�liku 2. k�lje pikkus => "))
S = b * c
print("Ristk�liku pindala", round(S, 1)) 
P = 2 * (b + c)
print("Ristk�liku �mberm��t", P)
di = sqrt(b**2 + c**2)  # Removed math.
print("Ristk�liku diagonaal", round(di, 2)) 
print()

print("Ringi karakteristikud")  # Removed round(d, 1) - d wasn't defined yet
r = float(input("Sisesta ringi raadiusi pikkus => ")) 
d = 2 * r 
print("Ringi l�bim��t", d) 
S = pi * r**2
print("Ringi pindala", round(S, 1))
C = 2 * pi * r
print("Ringjoone pikkus", round(C, 2))











