#Lav et program der beregner strømmen i et kabel og finder det rette kvadrat

P = int(input("Indtast effektforbrug på brugsgenstanden"))        # Indtast effektforbruget
U = 230                 # Spændingen er på 230V
I = P/U                 # Beregner strømmen
print(str(I)+" A")      # skriver amperer

taller=int(input("Skal der benyttes 70c kabel(tast 0) 90c kabel (tast 1)"))
#Taller bruges til checke om programmet skal stoppe(1) eller forsæt
