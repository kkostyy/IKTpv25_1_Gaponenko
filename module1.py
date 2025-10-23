#Harjutus 1
#k=0
#for i in range (15):
#    while True:
#        try:
#            arv = float(input(f"Sisesta {i+1}. arv: "))
#            break
#        except:
#            print("Palun sisesta arv!")
#
#    arv = float(input(f"Sisesta {i+1}. arv: "))
#    if int(arv)==arv:
#        print(f"{arv} on täisarv.")
#        k+=1
#print(f"Kokku oli {k} täisarvu.")
#
#Harjutus 2
#A = int(input("Sisesta arv A: "))
#summa = 0
#i = 1
#while True:
#    if i > A:
#        break
#    summa += i
#    i += 1
#print(f"Summa 1 kuni {A} on {summa}.")
#
#Harjutus 3
#korrutis = 1
#for i in range(8):
#    while True:
#        try:
#            arv = float(input(f"Sisesta {i+1}. arv: "))
#            break
#        except:
#            print("Palun sisesta arv!")
#    if arv > 0:
#        korrutis *= arv
#print("f>Positiivsete arvude korrutis on {korrutis}.")
#
#Harjutus 4
#for i in range(10, 21):
#    print(f"{i}² = {i**2}")
#
#Harjutus 5
#N = int(input("Sisesta N: "))
#summa = 0
#i = 0
#while True:
#    if i >= N:
#        break
#    try:
#        arv = float(input(f"Sisesta {i+1}. arv: "))
#        if arv < 0:
#            summa += arv
#        i += 1
#    except:
#        print("Palun sisesta arv!")
#print(f"Negatiivsete arvude summa on {summa}.")
#
#Harjutus 6
#N = int(input("Sisesta N: "))
#neg = pos = nul = 0
#i = 0
#while True:
#    if i >= N:
#        break
#    try:
#        arv = float(input(f"Sisesta {i+1}. arv: "))
#        if arv < 0:
#            neg += 1
#        elif arv > 0:
#            pos += 1
#        else:
#            nul += 1
#        i += 1
#    except:
#        print("Palun sisesta arv!")
#print(f"Negatiivseid: {neg}, Positiivseid: {pos}, Nulle: {nul}")
#
#Harjutus 7
#A = int(input("Sisesta A: "))
#B = int(input("Sisesta B: "))
#K = int(input("Sisesta K: "))
#i = A
#while True:
#    if i > B:
#        break
#    if i % K == 0:
#        print(i, end=" ")
#    i += 1
#print()
#
#Harjutus 8

