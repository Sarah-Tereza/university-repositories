lista=[]
while len(lista)<20:
    n=int(input('digite um número:'))
    if n in lista:
        print('a lista já possui esse valor, por favor digitar outro')
    elif n<40:
        print('digite um número maior que 40')
    else:
        lista.append(n)
print(lista)

