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