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