# Lav et Regnemaskine program?
#De 4 regnearter skal kaldes via funktioner
#Udfyld resten så programmet kommer til virke

def Plus(x,y):
    resultat =x+y
    return resultat

def Minus(x,y):


def Gange(x,y):


def Divider(x,y):


def menu():
    print("Tast 1(+), 2(-), 3(*), 4(/), 5(slut)")

menu()
Menutal = int(input("tast tal nu!!"))

while Menutal==1:
    print("Nu skal der lægges sammen(+)!")
    tal1=float(input("Indtast det første tal?"))
    tal2=float(input("Indtast det andet tal?"))
    print("Resultatet af",tal1,"+",tal2,"=",Plus(tal1, tal2))
    print()
    menu()
    Menutal = int(input("tast tal nu!!"))

while Menutal==2:


while Menutal==3:


while Menutal==4:



while Menutal==5:
    print("Slut!!!!!!!")
    break
