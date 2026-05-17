lista=[]
for k in range (5):
    lista.append(int(input('digite um valor')))
n1=int(input("digite a posição :"))
while (n1<0 or n1>4):
    n1=int(input("posção invalida, digite novamente:"))

n2=int(input("digite a posição"))
while (n2<0 or n2>4):
    n2=int(input("posição invalida, digite novamente:"))
print (lista)
print(lista[n1], lista[n2])