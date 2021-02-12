import datetime

x = datetime.datetime.now()
navn=input("hvad er dit navn?")
år=int(input("Hvilket år er du født?"))
print("Du hedder",navn,"og du er",x.year-år,"år gamle")
print(x.year)#x.year er året i år
print(x.day)#x.day er nummeret på dagen i måneden.
print(x.month)#x.month er nummeret på måneden i dag.
