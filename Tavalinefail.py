from Modulefail import *

print("Lahendame/testimime 5 arvutehet!")
for i in range(5):

    arv1= float_kontroll(input("Sisestada esimene arv: "))
    arv2= float_kontroll(input("Sisestada teine arv: "))
    
t=input("Sisesta tehe(+,-,*,/): ")
tulemus=arithmetic(arv1,arv2,t)
print(f"{arv1}{t}{arv2} = {tulemus}")
