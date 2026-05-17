numbers=[]
for k in range(15):
    numbers.append(int(input('digite um número:')))
print(f'o número 10 apareceu {numbers.count(10)} vezes')
for n in range(len(numbers)):
    if numbers[n] == 10:
        print(f'ele apareceu na seguinte posição:{n}')

        