"""
5) Elaborar um programa que o usuário deve digitar 15 números inteiros
(esses números devem ser armazenados em uma lista). Depois o programa deve mostrar:
quantas vezes o número 10 apareceu e em quais posições o número 10 foi encontrado.
"""

numbers = []

for k in range(15):
    numbers.append(int(input('digite um número: ')))

print(f'o numero 10 apareceu {numbers.count(10)} vezes')

for n in range(len(numbers)):
    if numbers[n] == 10:
        print(f'ele apareceu na seguinte posição: {n}')
