"""
2) Elaborar um programa que o usuário deve digitar 8 números reais (esses números
devem ser armazenados em uma lista) e depois o programa deve mostrar: todos os números
digitados, o maior número, o menor número e a diferença entre o maior e o menor valor.
"""

num = []
for x in range(8):
    num.append(float(input('digite o número: ')))

print(f'os numeros digitados são estes {num}')
print(f'esse é o maior número digitado: {max(num)}')
print(f'esse é o menor número digitado: {min(num)}')
print(f'essa é a diferença entre o maior e o menor: {max(num) - min(num)}')
