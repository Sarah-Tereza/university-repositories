#Elaborar um programa que contém uma matriz 4x4. O usuário deve preencher essa matriz. 
#Depois disso, o programa deve substituir: todos os números pares por 1, todos os números 
#ímpares por 0 e ao final, exibir a nova matriz.

matriz=[]
for a in range(4):
    lista=[]
    for b in range(4):
        num=float(input('digite um número:'))
        if num%2==0:
            lista.append(1)
        else:
            lista.append(0)
    matriz.append(lista)
print(f'essa é a nova matriz:{matriz}')