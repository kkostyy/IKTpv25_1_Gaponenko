l=[]
print(f"Listi algseis: {l}")
while True:
    print("Tee valik:")
    print("1-Lisa elemente\2-Lisa elemente pos-le\3-Emalda elementepos jargi")
    print("")

    while True:
        try:
            valik=int(input())
            break
        except:
            print("Arvud: 1...n")
    print("Töö listiga")
    if valik==1:
        while True:
            try:
                i=int(input("Mitu elementi soovid lisada? "))
                if i>0:
                    break
                else:
                    print("Arvud on vaja >0")
            except:
                print("Täisarvud on vaja kasutada")
        for element_id in range(i):
            element_id = input(f"{element_id}. element: ")
            l.append(element)
        print(f"Uuendatud list on {l}")
    elif valik==2:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soovid lisada (0-{len(l)}): "))
                if 0<=pos<=len(l):
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)}")
            except:
                print("Täisarvud on vaja kasutada")
        element = input("Sisesta element mida soovid lisada: ")
        l.insert(pos, element)
    elif valik==3:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soovid emalda (0-{len(l)-1}): "))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)-1}")
            except:
                print("Täisarvud on vaja kasutada")
        eem.element = l.pop(pos)
        print(f"Eemaldatud element on {eem_element}")
    elif valik==4:
        element = input("Sisesta element mida soovid eemaldada: ")
        mitu = l.count(element)
        if mitu == 0:
            print("Elementi ei leitud")
        else:
            for e in range(mitu):
                print(f"Eemaldatud element '{element}' {l.index(element)} poeitsioonilt")
                l.remove(element)
        print(f"Eemaldatud {mitu} elementi")
    elif valik == 5:
        while True:
            data = input("Sisesta elemendid komadega (või jäta tühjaks, et katkestada): ")
            if data.strip() == "":
                print("Tegevus katkestatud.")
                break
            uus_list = [x.strip() for x in data.split(",")]
            if len(uus_list) == 0:
                print("Midagi ei sisestatud. Proovi uuesti.")
                continue

            l.extend(uus_list)
            print("Listi laiendatud:", l)
            break

    elif valik == 6:
        while True:
            if len(l) == 0:
                print("List on tühi — midagi pole sorteerida.")
                break

            print("Kas soovid listi sorteerida? (jah/ei)")
            ans = input("> ").lower()

            if ans == "ei":
                print("Tegevus katkestatud.")
                break

            if ans == "jah":
                try:
                    l.sort()
                    print("List on sorteeritud:", l)
                except:
                    print("Viga: erinevat tüüpi elemendid — sorteerimine pole võimalik.")
                break

            print("Palun sisesta 'jah' või 'ei'.")



    print(f"Uuendatud list on {l}")


#extend(L)	Lisab kõik teise listi elemendid lõppu	loend.extend([6,7])
#sort()	Sorteerib listi	loend.sort()
#reverse()	Pöörab järjekorra ümber	loend.reverse()
#clear()	Tühjendab listi	loend.clear()