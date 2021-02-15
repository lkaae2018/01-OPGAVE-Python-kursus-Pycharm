Ofc1={"dB":5,"Lambda":1310,"Pris":250}
Ofc2={"dB":6,"Lambda":1310,"Pris":300}
Ofc3={"dB":7,"Lambda":1550,"Pris":350}
Ofc4={"dB":9,"Lambda":1550,"Pris":400}
Ofc5={"dB":11,"Lambda":1550,"Pris":600}
Ofc6={"dB":15,"Lambda":1550,"Pris":780}
Ofc7={"dB":20,"Lambda":1550,"Pris":1220}
Ofc=[Ofc1,Ofc2,Ofc3,Ofc4,Ofc5,Ofc6,Ofc7]
print("Vælg hvilken SFP du vil bruge til din beregning?")
for n in range(0,7):
    print("SFP nr.",n,Ofc[n])

print("Slut")
valg=int(input("Indtast tallet?"))

print(Ofc[valg]["dB"],"dB")
print(Ofc[valg]["Lambda"],"nm")
print(Ofc[valg]["Pris"],"Kr.")
