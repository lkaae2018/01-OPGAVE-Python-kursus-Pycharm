#Lave et program der udregner ohm lov i alle kombinationer!
def state0():

    indtast=input("Vil du udregne I, U, R eller P? Tryk bogstavet eller et andet for at stoppe")

    if indtast=="I" or indtast=="i":
        return I()
    elif indtast=="R" or indtast=="r":
        return R()
    elif indtast=="U" or indtast=="u":
        return U()
    elif indtast=="P" or indtast=="p":
        return P()
    else:
        return None

def I():
    indtast=input("Har U og R værdi så tryk U, har P og U værdien så tryk P")
    if indtast=="P" or indtast=="p":
        return UP()
    elif indtast=="U" or indtast=="u":
        return UR()
    else:
        return state0()
