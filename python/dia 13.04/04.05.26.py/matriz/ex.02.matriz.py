matriz=[]
soma=0
qnt=0
for i in range (3):
    linha=[]
    for j in range (3):
        valor=int(input("digite um numero:"))
        soma=soma+valor
        qnt= qnt+1
        linha.append(valor)
    matriz.append (linha)
media= soma/qnt
print(f'essa é a media :{media}essa é a qunatidade{qnt}')
for i in range (3):
    for j in range (3):
        if matriz[i][j]>media:
            print(matriz[i][j])