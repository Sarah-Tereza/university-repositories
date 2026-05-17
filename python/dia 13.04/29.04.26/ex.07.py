temperatura=[]
temp=float(input(" insira a temperatura:"))
print("digite 0 ou inferior para encerrar")
while temp > 0:
    temperatura.append(temp)
    temp=float(input("insira outra temperatura:"))
print(temperatura)
for x in range(len(temperatura)):
    if temperatura[x] and temperatura[x]<10:
        print(temperatura[x], '=frio')
    elif temperatura[x]>=10 and temperatura[x]<30:
        print(temperatura[x], "=agradável")
    elif temperatura[x]>=30 and temperatura[x]<60:
        print(temperatura[x],"=quente")
