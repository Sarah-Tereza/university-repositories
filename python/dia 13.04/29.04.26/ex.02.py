lista=[]
i=0
for k in range(5):
    n=int(input("digite um numero:"))
    lista.append(n)
    i=i+n
media= i/5
print(f"essa é a media:{media}")
mm=[]
for valor in lista:
    if valor > media:
        mm.append(valor)
print(f"esses são os valores maiores que a media: {mm}")
print(f"essa é a lista:{lista}")