# import msvcrt
# täht=""
# while True:
#     t=msvcrt.getwch()
#     print(t.replace(t,"*"),end="",flush=True)
#     täht+=t
#     if t=="\r":
#         break
# print()
# print(täht)

# täht=input("Sisesta oma nimi: ").encode('utf-8')
# print(f"Tere, {täht.decode('utf-8')}!")

import random

valikud = ["kivi", "käärid", "paber"]
punktid = {"Mängija1": 0, "Mängija2": 0}

while True:
    m1 = input("Mängija1, sisesta kivi, käärid või paber (või 'stop'): ").lower()
    if m1 == "stop":
        break
    m2 = input("Mängija2, sisesta kivi, käärid või paber (või 'stop'): ").lower()
    if m2 == "stop":
        break
    
    print(f"Mängija1: {m1}, Mängija2: {m2}")
    
    if m1 == m2:
        print("Viik!")
    elif (m1 == "kivi" and m2 == "käärid") or (m1 == "käärid" and m2 == "paber") or (m1 == "paber" and m2 == "kivi"):
        print("Mängija1 võitis!")
        punktid["Mängija1"] += 1
    else:
        print("Mängija2 võitis!")
        punktid["Mängija2"] += 1
    
    print("Punktid:", punktid)

