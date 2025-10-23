print("Tere! Olen sinu uus sõber - Python!")

nimi = input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")

valik = input(f"{nimi}! Kas leian Sinu keha indeksi? 0 - ei, 1 - jah => ")

if valik == "1":
    while True:
        try:
            pikkus = int(input("Palun sisesta oma pikkus sentimeetrites: "))
            if 0 < pikkus <= 250:
                mass = float(input("Palun sisesta oma kehakaal kilogrammides: "))
                if 0 < mass <= 350:
                    kmi = mass / ((pikkus / 100) ** 2)
                    print(f"{nimi}! Sinu keha indeks on:", kmi)
                    if kmi < 16:
                        hinnang = "Tervisele ohtlik alakaal"
                    elif 16 <= kmi <= 19:
                        hinnang = "Alakaal"
                    elif 20 <= kmi <= 25:
                        hinnang = "Normaalkaal"
                    elif 26 <= kmi <= 30:
                        hinnang = "Ülekaal"
                    elif 31 <= kmi <= 35:
                        hinnang = "Rasvumine"
                    elif 36 <= kmi <= 40:
                        hinnang = "Tugev rasvumine"
                    else:
                        hinnang = "Tervisele ohtlik rasvumine"
                    print("Hinnang:", hinnang)
                    break
                else:
                    print("Mass peab olema vahemikus 0 kuni 350 kg.")
            else:
                print("Pikkus peab olema vahemikus 0 kuni 250 cm.")
        except:
            print("Midagi läks valesti! Palun sisesta õiged arvud.")
elif valik == "0":
    print("Kahju! See on väga kasulik info!\n")
else:
    print("Vigane valik! Palun käivita programm uuesti ja vali 0 või 1.")

print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
#
