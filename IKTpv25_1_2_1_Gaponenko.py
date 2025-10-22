#1. Juku
#def on_juku_kinno():
#    eesnimi = input("Sisesta eesnimi: ")
#    if eesnimi == "JUKU":
#        print("Lahme Jukuga kinno!")
#    else:
#        print("Nimi pole kirjutatud suurtahtedega 'JUKU'.")
#    
#    vanus_str = input("Sisesta Juku vanus: ")
#    if vanus_str.isdigit():
#        vanus = int(vanus_str)
#        if vanus < 0 or vanus > 100:
#            print("Viga andmetega: vanus peab olema vahemikus 0 kuni 100.")
#        elif vanus < 6:
#            print("Pilet: TASUTA")
#        elif 6 <= vanus <= 14:
#            print("Pilet: Lastepilet")
#        elif 15 <= vanus <= 65:
#            print("Pilet: Taispilet")
#        else:
#            print("Pilet: Sooduspilet")
#    else:
#        print("Vanus peab olema taisarv.")
#on_juku_kinno()

#2 Pinginaabrid
#nimi1 = input("Sisesta nimi =>").capitalize()
#nimi2 = input("Sisesta nimi =>").capitalize()
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1 == "Konstantin" and  nimi2 == "Sofia" or nimi1 == "Sofia" and  nimi2 == "Konstantin":
#        print(f"{nimi1} ja {nimi2} on täna pinginaaberid")
#    else:
#        print(f"{nimi1} ja {nimi2} ei ole täna pinginaaberid")
#else:
#    print("Sisesta tähed!")


#3 Remont
#pikkus = int(input("Sisesta toa pikkus => "))
#laius = int(input("Sisesta toa laius => "))
#
#if pikkus > 0 and laius > 0:
#
#   pindala = pikkus * laius
#    print(f"Toa pindala on {pindala} ruutmeetrit.")
#    user = input("Kas soovid remondi? (jah/ei) => ").capitalize()
#    if user.isalpha() and user == "Jah":
#        hind = float(input("Sisesta remondi hind => "))
#        if hind > 0:
#            remondi_hind = hind * pindala
#            print(f"Remondi hind on {remondi_hind} eurot.")
#            kes = input("Kes teeb remondi? (ise/tootaja) => ").capitalize()
#            if kes.isalpha() and kes == "Ise":
#                print(f"{remondi_hind} eurot on remondi hind.")
#            else:
#                print(f"{remondi_hind * 1.2} eurot on remondi hind koos tootaja palgaga.")
#        else:
#            print("Hind ei saa olla  negatiivne!")
#    else:
#      print("Head aega!")
#else: user.isalpha() and user == "Ei":print("Remonti ei soovita.")
    
#4 Allahindus

#Leia 30% soodustusega hinna, kui alghind on suurem kui 700



#hind = input("Hind:")
#
#if hind.isdigit():
#    hind = float(hind)
#    if hind > 700:
#        hind *= 0.7
#        print(f"Soodus hind võrdub {hind}")
#else:
#    print("On vaja numbri sissetsda")


#5 Temperatuur
#try:
#    t=float(input("Sisesta temperatuur => "))
#    if t > 18:
#        print("soovitav toasoojus talvel")
#    else:
#        print("toasoojus pole soovitav talvel")
#except:
#    print("Palun sisesta temperatuur ujukomaarvuna!")

#6Pikkus
#def pikkus_hinnang():
#    pikkus_str = input("Sisesta oma pikkus cm: ")
#    if pikkus_str.isdigit():
#        pikkus = int(pikkus_str)
#        if pikkus < 160:
#            print("Sa oled lühike.")
#        elif 160 <= pikkus <= 185:
#            print("Sa oled keskmise pikkusega.")
#        else:
#            print("Sa oled pikk.")
#    else:
#        print("Sisesta täisarv.")
#
#pikkus_hinnang()

#7 Pikkus ja sugu
#def pikkus_ja_sugu():
#   pikkus_str = input("Sisesta oma pikkus cm: ")
#   sugu = input("Sisesta sugu (mees/naine): ").lower()
#   if pikkus_str.isdigit():
#       pikkus = int(pikkus_str)
#       if sugu == "mees":
#           if pikkus < 170:
#               print("Mees, oled lühike.")
#           elif 170 <= pikkus <= 190:
#               print("Mees, oled keskmise pikkusega.")
#           else:
#               print("Mees, oled pikk.")
#       elif sugu == "naine":
#           if pikkus < 155:
#               print("Naine, oled lühike.")
#           elif 155 <= pikkus <= 175:
#               print("Naine, oled keskmise pikkusega.")
#           else:
#               print("Naine, oled pikk.")
#       else:
#           print("Sugul peab olema 'mees' või 'naine'.")
#   else:
#       print("Sisesta täisarv pikkuse jaoks.")
#pikkus_ja_sugu()

#8 Poes
#import random

#def pood():
#    tooted = {
#       "piim": random.uniform(0.5, 1.5),
#        "sai": random.uniform(0.3, 1.0),
#        "leib": random.uniform(0.8, 2.0),
#        "muna": random.uniform(1.0, 3.0)
#    }
#    ostud = {}
#    for toode, hind in tooted.items():
#        vastus = input(f"Kas soovid osta {toode} (hind {hind:.2f} €)? (jah/ei) ").capitalize()
#        if vastus == "Jah":
#            kogus_str = input(f"Kui mitu {toode} soovid osta? ")
#            if kogus_str.isdigit():
#                kogus = int(kogus_str)
#                ostud[toode] = (hind, kogus)
#            else:
#                print("Sisesta korrektne kogus.")
#    
#    if ostud:
#        summa = 0
#       print("\n--- Tšekk ---")
#        for toode, (hind, kogus) in ostud.items():
#            summa_toode = hind * kogus
#            summa += summa_toode
#            print(f"{toode.title()}: {kogus} x {hind:.2f}€ = {summa_toode:.2f}€")
#        print(f"Kokku: {summa:.2f}€")
#    else:
#        print("Ostukorv on tühi.")
#
#pood()

#9 Ruut
#a_str = input("Sisesta esimese külje pikkus: ")
#b_str = input("Sisesta teise külje pikkus: ")
#if a_str.isdigit() and b_str.isdigit():
#    a = float(a_str)
#    b = float(b_str)
#    if a > 0 and b > 0:
#        if a == b:
#            print("Tegemist on ruuduga.")
#        else:
#            print("Tegemist ei ole ruuduga, vaid ristkülikuga.")
#    else:
#        print("Küljed peavad olema positiivsed.")
#else:
#    print("Sisesta arvud!")
#
#10 Matemaatika
#arv1_str = input("Sisesta esimene arv: ")
#arv2_str = input("Sisesta teine arv: ")
#if arv1_str.replace('.', '', 1).isdigit() and arv2_str.replace('.', '', 1).isdigit():
#    arv1 = float(arv1_str)
#    arv2 = float(arv2_str)
#    tehe = input("Vali tehe (+, -, *, /): ")
#    if tehe == "+":
#        print(f"Tulemus: {arv1 + arv2}")
#    elif tehe == "-":
#        print(f"Tulemus: {arv1 - arv2}")
#    elif tehe == "*":
#        print(f"Tulemus: {arv1 * arv2}")
#    elif tehe == "/":
#        if arv2 != 0:
#            print(f"Tulemus: {arv1 / arv2}")
#        else:
#            print("Nulliga ei saa jagada!")
#    else:
#        print("Tundmatu tehe.")
#else:
#    print("Sisesta arvud korrektselt!")
#
#11 Juubel
#vanus_str = input("Sisesta oma vanus: ")
#if vanus_str.isdigit():
#    vanus = int(vanus_str)
#    if vanus % 5 == 0:
#        print("Palju õnne! Sul on juubel! 🎉")
#    else:
#        print("Seekord ei ole juubel.")
#else:
#    print("Sisesta täisarv vanus!")
#
#12 Müük
#hind_str = input("Sisesta toote hind (€): ")
#if hind_str.replace('.', '', 1).isdigit():
#    hind = float(hind_str)
#    if hind <= 10:
#        soodus = hind * 0.9
#    else:
#        soodus = hind * 0.8
#    print(f"Lõplik hind on {soodus:.2f} €")
#else:
#    print("Sisesta korrektne hind!")
#
#13 Jalgpalli meeskond
#sugu = input("Sisesta sugu (mees/naine): ").lower()
#if sugu == "mees":
#    vanus_str = input("Sisesta vanus: ")
#    if vanus_str.isdigit():
#        vanus = int(vanus_str)
#        if 16 <= vanus <= 18:
#            print("Sobid jalgpalli meeskonda!")
#        else:
#            print("Vanus ei sobi meeskonda.")
#    else:
#        print("Sisesta korrektne vanus!")
#elif sugu == "naine":
#    print("Antud meeskonda võetakse ainult mehi.")
#else:
#    print("Sisesta 'mees' või 'naine'.")
#
#14 Busside logistika
#inimesed_str = input("Sisesta inimeste arv: ")
#kohad_str = input("Sisesta kohtade arv ühes bussis: ")
#if inimesed_str.isdigit() and kohad_str.isdigit():
#    inimesed = int(inimesed_str)
#    kohad = int(kohad_str)
#    if inimesed > 0 and kohad > 0:
#        bussid = (inimesed + kohad - 1) // kohad
#        viimases = inimesed % kohad if inimesed % kohad != 0 else kohad
#        print(f"Vaja on {bussid} bussi.")
#        print(f"Viimases bussis on {viimases} inimest.")
#    else:
#        print("Arvud peavad olema positiivsed!")
#else:
#    print("Sisesta täisarvud!")




