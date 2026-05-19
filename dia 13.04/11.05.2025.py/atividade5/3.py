p=[]
n=[]
numbers=[]
for x in range(12):
    numbers.append(int(input('digite o número:')))
for e in numbers:
    if e > 0:
        p.append(e)
    elif e < 0:
        n.append(e)

print(f'esses são os positivos:{p}')
print(f'esses são os negativos:{n}')
print(f'total de zeros:{numbers.count (0)}')

