def sum_two_numbers(a, b):
    return a + b            # returnere summen af de 2 tal a, b

c = sum_two_numbers(3, 12)  # variablen c tildeles summen af a og b

def to_tal(x, y):
    #global c
    c=x+y
    return c


print(to_tal(1, 3))
print(c)
