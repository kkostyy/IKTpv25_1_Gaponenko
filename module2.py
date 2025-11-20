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

    print(f"Uuendatud list on {l}")
