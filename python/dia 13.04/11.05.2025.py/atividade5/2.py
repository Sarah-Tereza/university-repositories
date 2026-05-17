num=[]
for x in range(8):
    num.append(float(input('digite o número:')))
print (f'os numeros digitados são estes {num}')
print (f'esse é o maior número digitado:{max(num)}')
print (f'esse é o menor número digitado:{min(num)}')
print (f'essa é a diferença entre o maior e o menor:{max(num)-min(num)}')

