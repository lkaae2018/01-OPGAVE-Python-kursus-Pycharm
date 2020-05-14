#Statemachine til beskrivelse af livets gang
import time

y=0
tid=1

def Home(x):
    global y
    global tid
#Lav en tæller som stoppet livet!!!
    if x=="wake":
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


def Bed(x):



state=Home(x="wake")
while state: state=Home(x="wake")
print("Død og færdig!!!!")




