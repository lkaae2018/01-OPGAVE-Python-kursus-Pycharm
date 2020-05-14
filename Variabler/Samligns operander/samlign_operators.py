en = 1
to = 2
tre = 3

print(en < to < tre)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

er_større = tre > to
print(er_større)

print((en > to) or (to < tre))
