#Elaborar um programa em que o usuário deve preencher uma matriz 4x3 com números 
#inteiros. Após isso, o programa deve exibir: a soma de cada linha e a soma de cada coluna.

matriz=[]
coluna=0
soma=0
for a in range(4):
    linha=[]
    for b in range(3):
        valor=int(input('digite um numero:'))
        linha.append(valor)
    matriz.append(linha)
for b in range(3):
    soma=0
    elementos=[]
    for coluna in matriz:
        soma+= coluna[b]
        elementos.append(coluna[b])
    print(f'coluna:[{b}], elementos:{elementos}')
    print(f'soma dos elementos:{soma}')
for a in range(4):
    print(f'linha:{[a]}, elementos:{matriz[a]}')
    print(f'soma:{sum(matriz[a])}')