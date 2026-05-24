"""
3) Elaborar um programa que contém uma lista com 20 elementos. Essa lista deve ser
preenchida pelo usuário, porém não deve conter valores repetidos e valores abaixo de 40. Exibir
no final a lista com os 20 elementos.
"""

lista=[]
while len(lista)<20:
    n=int(input('digite um numero: '))
    if n in lista:
        print('a lista ja possui esse valor, por favor digitar outro: ')
    elif n<40:
        print('digite um numero maior que 40: ')
    else:
        lista.append(n)
print(lista)
