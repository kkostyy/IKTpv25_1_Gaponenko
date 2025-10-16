paev=imput("Sisesta päev nimetus(nt. esmaspäev) => "))")
#1. Kui on neljapäev, siis "Huraaa, Prgrameerimine!"
if paev.lower()=="neljapäev":
    print("Huraaa, Prgrameerimine!")

#2. Kui on neljapäev, siis "Huraaa, Prgrameerimine!", kui on reede, siis "Igatsen, programmeerimida tahaks!"
if paev.lower()=="neljapäev":
    print("Huraaa, Prgrameerimine!")
else if paev.lower()=="reede":
    print("Igatsen, programmeerimida tahaks!")

#3. Tööpaevad ja nädalavahetus
if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("Tööpäev, pean tööl käima!")

# 1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
paev_number = int(input("Siseta päeva number (1-7): "))
if paev_number == 1:
    print("Esmaspäev")
elif paev_number == 2:
    print("Teisipäev")
elif paev_number == 3:
    print("Kolmapäev")
elif paev_number == 4:
    print("Neljapäev")
elif paev_number == 5:
    print("Reede")
elif paev_number == 6:
    print("Laupäev")
elif paev_number == 7:
    print("Pühapäev")
else:
    print("Vale number! Palun sisesta nimber vahemikus 1-7.")