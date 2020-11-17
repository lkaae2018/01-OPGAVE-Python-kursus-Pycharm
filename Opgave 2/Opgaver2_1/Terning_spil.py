import random
# Lav en program hvor du spiller terning imod maskinen
# Den er først vinder 10 gange skal stoppe spillet
# der skal trykkes på en tast mellem terning kast
# Tilslut skal i lave terningerne grafik
# Opret en .py file, hvor terningerne skal importeres fra
# _____________
# |  O     O   |
# |     O      |
# |  O      O  |
# ______________

def menu():
    print("Tryk på en tast for at starte terningmaskinen")
    print("Du spiller mod maskinen")
    x=input("Tryk på en enter for starte")

menu()

Dig=0
Maskine=0

while True:
    x=random.randrange(1,7)
    print("Du har slået en",x)
    y=random.randrange(1,7)
    print("Maskinen har slået en",y)
    menu()
    if x>y:
        Dig +=1
    elif y>x:
        Maskine += 1
    else:
        print("I slog samme tal!")
    #menu()
    print("Dig",x,"Maskine",y)
    if Dig==10 or Maskine==10:
        if Dig==10:
            print("Du vandt!!", Dig, "mod", Maskine)
        else:
            print("Makinen vandt!",Maskine,"mod dine", Dig)
        break
