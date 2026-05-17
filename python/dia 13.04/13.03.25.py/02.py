lista=[]
for x in range(10):
    lista.append(float(input('digite um numero:')))
reposta='s'
achar= False
while reposta.lower()=='s' and not achar:
    x=float(input('qual valor dejesa achar:'))
    if lista.count(x) > 0:
        print('valor encontrado')
        print(f'posição:{lista.index(x)}')
        achar=True
    else:
        print('valor não existe!')
        resposta=input('deseja continuar a busca?(s/n):')