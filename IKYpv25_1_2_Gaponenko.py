paev=imput("Sisesta p�ev nimetus(nt. esmasp�ev) => "))")
#1. Kui on neljap�ev, siis "Huraaa, Prgrameerimine!"
if paev.lower()=="neljap�ev":
    print("Huraaa, Prgrameerimine!")

#2. Kui on neljap�ev, siis "Huraaa, Prgrameerimine!", kui on reede, siis "Igatsen, programmeerimida tahaks!"
if paev.lower()=="neljap�ev":
    print("Huraaa, Prgrameerimine!")
else if paev.lower()=="reede":
    print("Igatsen, programmeerimida tahaks!")

#3. T��paevad ja n�dalavahetus
if paev.lower()=="laup�ev" or paev.lower()=="p�hap�ev":
    print("L�puks ometi n�dalavahetus!")
else:
    print("T��p�ev, pean t��l k�ima!")

# 1-esmasp�ev, 2-teisip�ev, 3-kolmap�ev, 4-neljap�ev, 5-reede, 6-laup�ev, 7-p�hap�ev
paev_number = int(input("Siseta p�eva number (1-7): "))
if paev_number == 1:
    print("Esmasp�ev")
elif paev_number == 2:
    print("Teisip�ev")
elif paev_number == 3:
    print("Kolmap�ev")
elif paev_number == 4:
    print("Neljap�ev")
elif paev_number == 5:
    print("Reede")
elif paev_number == 6:
    print("Laup�ev")
elif paev_number == 7:
    print("P�hap�ev")
else:
    print("Vale number! Palun sisesta nimber vahemikus 1-7.")