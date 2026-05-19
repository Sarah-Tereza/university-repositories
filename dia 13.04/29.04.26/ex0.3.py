lista=[]
for k in range (5):
    lista.append(int(input("digite o numero")))
lista2=[]
for valor in lista:
    if valor%2 == 0:
        lista2.append(valor**2)
    else:
        lista2.append(valor**3) 
print(lista)
print(lista2) 