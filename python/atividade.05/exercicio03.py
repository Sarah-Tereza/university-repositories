"""
3) Elaborar um programa que o usuário deve digitar 12 números inteiros (esses números
devem ser armazenados em uma lista) e em seguida o programa deve mostrar: todos os números
positivos (armazenados em outra lista), todos os números negativos (armazenados em outra
lista), a quantidade de zeros digitados.
"""

p = []
n = []
numbers = []

for x in range(12):
    numbers.append(int(input('digite o número: ')))

for e in numbers:
    if e > 0:
        p.append(e)
    elif e < 0:
        n.append(e)

print(f'esses são os positivos: {p}')
print(f'esses são os negativos: {n}')
print(f'total de zeros: {numbers.count(0)}')
