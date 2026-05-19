matriz=[]
for i in range (4):
    linha=[]
    for j in range(4):
        linha.append(int(input('digite um numero:')))
    matriz.append(linha)
for i in range(4):
    for j in range (4):
        print(f'[{i}][{j}]={matriz[i][j]}')