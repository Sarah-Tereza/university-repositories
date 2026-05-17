lista=[]
for k in range(10):
    n=(int(input('digite um numero')))
    lista.append(n)
primos=[]
for n in lista:
    primo=True
    for x in range(2, int(n**0.5)+1):
        if n % x==0:
            primo=False
    if primo:
        primos.append(n)
print(lista, primos)