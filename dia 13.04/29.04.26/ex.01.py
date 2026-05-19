lista=[]
for k in range(16):
    lista.append(int(input("digite um numero:")))
num1=int(input(" digite a posição:"))
while num1<0 or num1>15:
    num1=int(input("posição invalida, digite novamente:"))

num2=int(input("digite outra posição:"))
while num2<0 or num2>15:
    num2=int(input('posição invalido, digite novamente:'))

print(lista)
soma= lista[num1]+lista[num2]
print(f'essa é a soma deles: {soma}')