from Modulefail import *


# Ülesanne 1 — Aritmeetika (5 tehet)
print("Lahendame / testime 5 arvutust!")
for i in range(5):
    arv1 = float_kontroll(input("Sisesta esimene arv: "))
    arv2 = float_kontroll(input("Sisesta teine arv: "))
    t = input("Sisesta tehe (+,-,*,/): ")
    tulemus = arithmetic(arv1, arv2, t)
    print(f"{arv1}{t}{arv2} = {tulemus}")
print("-" * 40)

# Ülesanne 2 — Liigaasta (3 kordust)
print("Kontrollime, kas aasta on liigaasta!")
for i in range(3):
    aasta = int_kontroll(input("Sisesta aasta: "))
    if is_year_leap(aasta):
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} on tavaline aasta")
print("-" * 40)

# Ülesanne 3 — RUUT
print("Arvutame ruudu ümbermõõdu, pindala ja diagonaali!")
külg = float_kontroll(input("Sisesta ruudu külje pikkus: "))
ümbermõõt, pindala, diagonaal = square(külg)

print(f"Ruudu külg: {külg}")
print(f"Ruudu ümbermõõt: {ümbermõõt}")
print(f"Ruudu pindala: {pindala}")
print(f"Ruudu diagonaal: {diagonaal}")
print("-" * 40)

# Ülesanne 4 — Aastaajad
kuu = int_kontroll(input("Sisesta kuu number (1–12): "))
print(f"Kuu {kuu} vastab aastaajale: {season(kuu)}")
print("-" * 40)

# Ülesanne 5 — Pangahoius
print("Arvutame pangahoiuse lõppsumma!")
a = float_kontroll(input("Sisesta hoiuse summa: "))
years = int_kontroll(input("Mitu aastat hoiad raha pangas?: "))
print("Lõppsumma:", bank(a, years))
print("-" * 40)

# Ülesanne 6 — Algarvud
arv = int_kontroll(input("Sisesta arv (0–1000): "))
print("Kas algarv?", is_prime(arv))
print("-" * 40)

# Ülesanne 7 — Kuupäev
print("Kontrollime, kas kuupäev eksisteerib!")
p = int_kontroll(input("Sisesta päev: "))
k = int_kontroll(input("Sisesta kuu: "))
a = int_kontroll(input("Sisesta aasta: "))
print("Kehtiv kuupäev:", date(p, k, a))
print("-" * 40)

# Ülesanne 8 — XOR krüpteerimine
print("XOR krüpteerimine!")
tekst = input("Sisesta tekst: ")
võti = int_kontroll(input("Sisesta võti: "))
krypt = XOR_cipher(tekst, võti)
print("Krüpteeritud:", krypt)
print("Dekrüpteeritud:", XOR_uncipher(krypt, võti))
print("-" * 40)

# Ülesanne 9 — Keskmine
print("Arvutame keskmise!")
lst = [1, 5, 7, 3, 9]
print("Järjend:", lst)
print("Keskmine:", average(lst))
print("-" * 40)

# Ülesanne 10 — Väikseim ja suurim
lst2 = [4, -2, 10, 7, 0]
print("Järjend:", lst2)
print("Min ja Max:", min_max(lst2))
print("-" * 40)

# Ülesanne 11 — Ainulaadsed elemendid
lst3 = [1, 2, 2, 3, 4, 4, 5, 1]
print("Originaal:", lst3)
print("Ainulaadsed:", unique_elements(lst3))
print("-" * 40)


