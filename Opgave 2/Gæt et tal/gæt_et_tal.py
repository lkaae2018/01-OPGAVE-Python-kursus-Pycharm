import random

tal=0 #Variable til gemme spilleren tal i
gæt=1 #Antal gæt der er foretaget

def menu(): #Hovedmenu
    while True:
        global tal
        tal=int(input("Indtast et tal mellem 0-10"))
        if tal < 0 or tal > 10:
            print("Tallet skal være mellem 0-10!") # Printes hvis tallet er undenfor området!!
            continue #Starter for i while loopen
        else:
            break #Returner til det sted der kalder på funktionen
def stort():
    global tal
    print("Du har lige gættet på",tal)
    tal=int(input("Indtast et tal der er mindre"))

def mindre():
    global tal
    print("Du har lige gættet på",tal)
    tal=int(input("Indtast et tal der er større"))

while True:
    menu()
    x=random.randrange(0,11)
    while True:
        if tal > x:

        elif tal < x:

        else:
            print("Du gættede rigtigt")
            print("Du gættede",gæt,"gange")
            forts = input("Vil du fortsætte(J/N)")
            if forts =="J" or forts == "j":
                break
            else:
                exit(0)

