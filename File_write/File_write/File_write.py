#https://www.tutorialspoint.com/python/python_files_io.htm
if __name__ == "__main__":
    File_navn=input("indtast navnet på filen, med ekstensions!")
    f = open(File_navn, "w") #Filen oprettes og hvis der eksistere en i forvejen overskrives den!

    string1=input("Indtast dit fornavn?")
    string1=string1+"\n" # \n laver en ny line i filen
    f.write(string1) #string1 skrives til filen
    f.close() # Filen lukkes ned

    f = open(File_navn, "a") # Filen åbnes og nu kan der adder noget tekst til den
    string2=input("Indtast dit efternavn?")
    string2=string2+"\n"+"Filens navn er:"+File_navn # \n laver en ny line i filen
    f.write(string2)
    f.close()

#Åben filen som er i projektmappe og se om den indeholder den tekst du skrev.
