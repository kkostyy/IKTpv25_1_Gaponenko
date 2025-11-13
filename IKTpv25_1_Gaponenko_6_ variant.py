# 1
n = int(input("Sisesta tornide arv (1–9): "))
for i in range(n):
    print("  Ä  ")
    print(" / \\ ")
    print(" | | ")
    print("  __ ")
    print()


# 2 
summa = 0
kuud = 12
for i in range(1, kuud + 1):
    kulu = int(input("Sisesta " + str(i) + ". kuu kulusumma: "))
    summa += kulu
keskmine = summa / kuud
print("Aastane keskmine kulusumma on:", keskmine)


# 3
M = float(input("Sisesta kanga pikkus meetrites: "))
alles = M
while True:
    vastus = input("Sisesta tüki pikkus (või 'stop'): ")
    if vastus == "stop":
        break
    pikkus = float(vastus)
    if pikkus <= alles:
        alles -= pikkus
        print("Lõigatud", pikkus, "m. Alles on", round(alles, 2), "m.")
    else:
        print("Materjali ei ole piisavalt.")

# 4
import random
L = int(input("Sisesta laius (L): "))
H = int(input("Sisesta kõrgus (H): "))
for i in range(H):
    for j in range(L):
        arv = random.randint(0, 9)
        print(arv, end=" ")
    print()


# 5
import random
tootajad = int(input("Sisesta töötajate arv: "))
A = int(input("Sisesta palkade piir (A eurot): "))
kokku = 0
for i in range(tootajad):
    palk = random.randint(800, 4000)
    vanus = random.randint(20, 75)
    print("Töötaja", i + 1, ": palk =", palk, "€, vanus =", vanus, "a.")
    if palk > A and vanus >= 65:
        kokku += 1
print("Pensioniealisi, kelle palk on üle", A, "€:", kokku)
