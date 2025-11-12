# 1
n = int(input("Sisesta jäneste arv (1-9): "))
for i in range(n):
    print("   (\\_/)")
    print("   (o o)")
    print("   / | \\*")
    print()

# 2 
L = int(input("Sisesta arv L: "))
summa = 0
for i in range(L + 1):
    summa += i
print("Summa 0 kuni", L, "on", summa)
print()

# 3
import random
salasona = random.randint(0, 100)
katsed = 0
print("Arva ära number (0–100). Sul on 10 katset.")
while katsed < 10:
    arva = int(input("Sisesta oma arv: "))
    katsed += 1
    if arva == salasona:
        print("Õige! Arvasid ära", katsed, "katsega!")
        break
    elif arva < salasona:
        print("Sinu arv on liiga väike!")
    else:
        print("Sinu arv on liiga suur!")
if arva != salasona:
    print("Ei arvanud ära. Õige vastus oli:", salasona)
print()

# 4
arv = input("Sisesta arv: ")
pööratud = arv[::-1]
print("Ümberpööratud arv on:", pööratud)
print()

# 5
arv = input("Sisesta täisarv: ")
summa = 0
korrutis = 1
for number in arv:
    number = int(number)
    summa += number
    korrutis *= number
print("Summa =", summa)
print("Korrutis =", korrutis)
