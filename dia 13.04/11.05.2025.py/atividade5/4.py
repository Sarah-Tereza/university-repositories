nomes=[]
qnt=0
for x in range(7):
    nomes.append(input('digite um nome:'))
print(f'esses são os nomes digitados:{nomes}')
print(f'primeiro nome digitado:{nomes[0]}')
print(f'ultimo nome digitado:{nomes[6]}')
for n in nomes:
    if len(n)>5:
        qnt += 1
print (f'quantidade de nomes com mais de 5 digitos:{qnt}')

