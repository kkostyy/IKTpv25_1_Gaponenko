print("Tere, maailm!")  

nimi = input("Mis on sinu nimi? ").capitalize
vanus = input("Kui vana sa oled? ") 

print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")



vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_kaib_koolis = True

print(type(vanus))
print(type(eesnimi))
print(type(pikkus))
print(type(kas_kaib_koolis))

import random

kommide_arv = random.randint(5, 20)  
print("Laual on", kommide_arv, "kommi.")

soov = int(input("Mitu kommi sa soovid ara votta? "))
kommide_arv -= soov

print("Nuud on laual", kommide_arv, "kommi.")



