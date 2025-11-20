l=[]
print(f"Listi algseis: {l}")
while True:
    print("1. Lisa element")
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
