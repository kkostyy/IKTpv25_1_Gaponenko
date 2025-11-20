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
