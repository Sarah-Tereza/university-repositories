lista=[]
i=0
a=0
for k in range (10):
   lista.append(int(input('digite um numero:')))
for x in range(len(lista)):
    if lista[x] % 2 == 0:
        print(f'{lista[x]}=par')
        i=i+1
    else:
        print(lista[x],'=impar')
        a=a+1
print(f'total de pares={i}')
print(f'total de impares={a}')
