#Elaborar um programa que contém uma matriz 4x4. O usuário deve preencher essa matriz. 
#Depois disso, o programa deve substituir: todos os números pares por 1, todos os números 
#ímpares por 0 e ao final, exibir a nova matriz.

matriz=[]
new_matriz=[]
for a in range(4):
    lista=[]
    for b in range(4):
        linha.append(float(input('digite um número:')))
    matriz.append(linha) 
print(f'essa é a matriz original{matriz}')

for a in range(4):
    new_linha=[]
    for b in range(4):
        if matriz[a][b]%2==0:
            new_lista.append(1)
        elif matriz[a][b] % 2 !=0:
            new_linha.append(0)
    matriz.append(new_linha)
print(f'essa é a nova matriz:{new_matriz}')
