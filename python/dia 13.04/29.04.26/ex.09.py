lista=[]
while len(lista) < 15:
    n=float(input('digite um numero:'))
    lista.append(n)
    for x in lista:
        if lista.count(x)>1:
            lista.remove(x)
lista.sort() 
print(lista)


