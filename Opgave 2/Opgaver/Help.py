while True:
    try:
         x = int(input("Indtast et tal:"))
         break
    except ValueError:
         	print("Det er ikke et tal, prøv igen")

#Forklaring: hvis der sker en fejl mellem try og except vil programmet spring til sidste linie.
while True:
    x=int(input("Indtast et tal"))
    if x==0:
        print("Du har tastet 0")
        continue
