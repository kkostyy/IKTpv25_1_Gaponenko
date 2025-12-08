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
#6
def is_prime(arv:int)->any:
    '''Kirjuta funktsioon is_prime,
    mis võtab ühe argumendi — arvu vahemikus 0 kuni 1000,
    ja tagastab True, kui see on algarv, ja False muul juhul.
    Kui arv on kordarv, kuva selle jagajad.
    '''
    if arv < 2 or arv > 1000:
        return "Arv peab olema vahemikus 0 kuni 1000"

    for i in range(2, int(arv**0.5) + 1):
        if arv % i == 0:
            print(f"{arv} ei ole algarv. Jagajad:")
            for j in range(2, arv):
                if arv % j == 0:
                    print(j, end=" ")
            print()
            return False
    return True


#7
def date(p:int, k:int, a:int)->bool:
    if k < 1 or k > 12 or p < 1:
        return False

    # päevade arv kuudes
    päevad = [31, 29 if is_year_leap(a) else 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

    return p <= päevad[k - 1]

#8
def XOR_cipher(sõne:str, võti:int)->str:
    return "".join(chr(ord(täht) ^ võti) for täht in sõne)

def XOR_uncipher(sõne:str, võti:int)->str:
    return "".join(chr(ord(täht) ^ võti) for täht in sõne)

#9
def average(numbers:list)->float|None:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

#10
def min_max(numbers:list)->tuple:
    return min(numbers), max(numbers)

#11
def unique_elements(lst:list)->list:
    uus = []
    for el in lst:
        if el not in uus:
            uus.append(el)
    return uus

