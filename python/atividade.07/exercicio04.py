# Elaborar um programa em que o usuário deve preencher uma matriz 5x2. Após isso, o 
#programa deve mostrar: todos os valores digitados e o maior valor de cada linha.

matriz=[]
maxvalor=0
for a in range(5):
    linha=[]
    for b in range(2):
        num=(int(input('digite um valor:')))
        linha.append(num)
    matriz.append(linha)

for a in range(5):
    print(f'linha:{a}, elementos:{matriz[a]}')
    print(f'esse é o maior valor:{max(matriz[a])}')
