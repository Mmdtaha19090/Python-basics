SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}
setA = list(SetA)
setB = list(SetB)
sum = setB + setA
eshterak = []
for i in setA:
    if i in setB:
        eshterak.append(i)
print(f"sum : {sum} , eshterak : {eshterak}")