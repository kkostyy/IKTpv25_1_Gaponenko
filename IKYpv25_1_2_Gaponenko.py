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