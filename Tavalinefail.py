from Modulefail import *

arv=int_kontroll(input)
aasta= int_kontroll(input)
a

kuu=int_kontroll(input("Sisesta kuu number (1-12): "))
print(f"Kuul {kuu} on aastaja {season(kuu)}")







print("arvutame ruudu pinala ja ümbermõõdu!")
külg=float_kontroll(input("Sisesta ruudu külje pikkus: "))
ümbermõõt,pindala, diagonaal=square(külg)
print(f"Ruudu külg: {külg}")
print(f"Ruudu ümbermõõt: {ümbermõõt}")
print(f"Ruudu pindala: {pindala}")
print(f"Ruudu diagonaal: {diagonaal}")




for i in range(3):
    aasta=int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} on tavaline aasta")



print("Lahendame/testimime 5 arvutehet!")
for i in range(5):

    arv1= float_kontroll(input("Sisestada esimene arv: "))
    arv2= float_kontroll(input("Sisestada teine arv: "))
    
    t=input("Sisesta tehe(+,-,*,/): ")
    tulemus=arithmetic(arv1,arv2,t)
    print(f"{arv1}{t}{arv2} = {tulemus}")


