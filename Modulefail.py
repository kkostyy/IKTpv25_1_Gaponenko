#Töö 5.1
#1
def float_kontroll(sisend:str)->float:
    """Kontrillib, kas sisestatud andmed on teisendatavad float arvuks
    :param str sisend: kasutaja sissestatud andmed
    :return/rtype: teisendatud float arv
    """
    while True:
        try:
            arv=float(sisend)
            return arv
        except ValueError:
            sisend=input("Palun sisesta arv: ")

def arithmetic(a:float,b:float,tehe:str)->any:
    """Lihtne kalkulaator:
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Muul juhul tagastab "Tundumatu tehe"
    :param float a: esimene arv
    :param float b: teine arv
    :param srt tehe: tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    if tehe in ["+","-","*","/"]:
        if tehe=="/" and b==0:
            vastus = "Nulliga jagamine pole lubatud"
        else:
            vastus = eval(f"{a}{tehe}{b}")
    else:
        vastus = "Tundumatu tehe"
    return vastus

#2

def is_year_leap(aasta:int)->bool:
    """Kontrollib, kas aasta on liigaasta
    :param int aasta: aasta arvuna
    :return/rtype: True kui liigaasta, False kui tavaline aasta
    """
    if (aasta % 4 == 0 and aasta % 100 != 0):
        return True
    else:
        return False

def int_kontroll(sisend:str)->int:
    """Kontrillib, kas sisestatud andmed on teisendatavad int arvuks
    :param str sisend: kasutaja sissestatud andmed
    :return/rtype: teisendatud int arv
    """
    while True:
        try:
            arv=int(sisend)
            return arv
        except ValueError:
            sisend=input("Palun sisesta arv: ")

#3 
def square(külg:float)->any:
    ümbermõõt=4*külg
    diagonaal=külg**0,5*2
    pindala=külg**2
    return ümbermõõt, pindala, diagonaal

#4
def season(kuu:int)->str:
    if kuu in [12, 1, 2]:
        return "talv"
    elif kuu in [3, 4, 5]:
        return "kevad"
    elif kuu in [6, 7, 8]:
        return "suvi"
    elif kuu in [9, 10, 11]:
        return "sügis"
    else:
        return "vigane kuu"

#5
def bank(a:float,aasta:int)->float:
    """Kasutaja teeb hoiuse summas a eurot years aastaks 10% aastaintressiga 
    (igal aastal suureneb hoiusumma 10%, ka intressile arvestatakse järgmise aasta intress).
    Kirjuta funktsioon bank, mis võtab argumendid a ja years,
    ning tagastab lõppsumma kasutaja kontol.
    """
    intress=0.1
    for i in range(aasta):
        a+=a*intress
    return a