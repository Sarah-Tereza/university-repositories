a=[]
for x in range(5):
    a.append(int(input('digite um numero:')))
b=[]
for valor in a:
    if valor <5:
        b.append("funcionou")
        b.append(valor)
print(a + b)