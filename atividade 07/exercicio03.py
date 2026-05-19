#Elaborar um programa que contém uma matriz 3x4. O usuário deve preencher essa matriz. 
#Após isso, o programa deve exibir: todos os valores maiores que 20, a quantidade de 
#valores maiores que 20 e suas posições na matriz.

matriz=[]
for a in range(3):
    linha=[]
    for b in range(4):
        num=float(input('digite um numero:'))
        linha.append(num)
    matriz.append(linha)
qnt=0
print(f'valores maiores que 20 e suas posições:')
for a in range(3):
    for b in range(4):
        if matriz[a][b] >20:
            print(f'{matriz[a][b]},linha={a},coluna={b}')
            qnt+=1

print(f'esses é o total de vezes que aparecem:{qnt}')