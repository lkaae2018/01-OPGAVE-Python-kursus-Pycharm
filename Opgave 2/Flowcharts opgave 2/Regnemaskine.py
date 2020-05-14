#Regnemaskine lavet while loops
x=0
y=0
operator=0

def menu():
    global x #Global variable
    global y #Global variable
    global operator #Global variable
    x=float(input("Indtast et tal mellem 0 og 1000"))
    y=float(input("Indtast et tal mmelm 0 og 1000"))
    operator=input("Vælg mellem *,-,+,/")
menu()

while True:

    while operator=="+":

    while operator=="-":

    while operator=="*":

    while operator=="/":


    while operator !="-" or operator!= "+" or operator!= "*" or operator!= "/":
        print("Ingen af tegnene valgt")
        print("Programmet stopper!")
        exit(0)

