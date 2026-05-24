#elaborar um programa que contém uma matriz 5x5. O usuário deve preencher essa matriz 
#com números inteiros. Após isso, o programa deve exibir: a soma de todos os valores da 
#matriz, a média dos valores e o maior valor digitado.

matriz=[]
total=0
qnt=0
max=0
for a in range(5):
    linha=[]
    for b in range(5):
        valor=int(input('digite um número:'))
        total+=valor
        qnt= qnt+1
        linha.append(valor)
        if valor > max:
            max=valor
    matriz.append(linha) 
for a in range(5):
    print(f'linha:{a}')
    for b in range(5):
        print(f'numero:{matriz[a][b]}')
print(f'essa é a soma de todos os valores:{total}')
print(f'essa é a média da matriz:{total/qnt}')
print(f'esse é o maior valor na matriz:{max}')
