'''
4) Elaborar um programa que contém uma matriz 4x5. O usuário deve preencher essa
matriz com números reais. Após isso, o programa deve calcular a média de cada linha e exibir
qual linha possui a maior média.
'''

matriz=[]
q=0
m=0
maior=0
posição=0
for a in range(4):
    linha=[]
    for i in range (5):
        n=float(input('digite um numero: '))
        linha.append(n)
    matriz.append(linha)
for a in range(4):
    m=0
    q=0
    for i in range (5):
        m = m+matriz[a][i]
        q = q+1
    media = m/q
    if media > maior:
        maior=media
        posição= a
    print(f'Linha:{a} media:{media} qnt:{q}')
print(f' a maior média está na linha:{posição}')
