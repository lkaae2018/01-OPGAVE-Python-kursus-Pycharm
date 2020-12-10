#Statemachine til beskrivelse af livets gang
import time

y=0
tid=1
week=5
def weekend():
    print("Weekend i 2 dage")
    x="wake"
    return Home(x)

def Home(x):
    global week
    global y
    global tid

    if week==0:
        y+=2
        week=5
        return weekend()

    if y==50:
        return
    if x=="wake":
        y+=1
        week-=1
        print("Dag=",y)
        x="take train"
        print("Tager toget på arbejde")
        time.sleep(tid)
        return Work(x)
    elif x=="take train":
        x="sleep"
        print("Går i seng")
        time.sleep(tid)
        return Bed(x)

def Work(x):
    if x=="take train":
        x="take train"
        print("Tager toget hjem fra arbejde")
        time.sleep(tid)
        return Home(x)

def Bed(x):
    if x=="sleep":
        x="wake"
        print("Vågner")
        time.sleep(tid)
        return Home(x)


state=Home(x="wake")
while state: state=Home(x="wake")
print("Død og færdig!!!!")




