produto=[]
qnt=[]

for  x in range(5):
    produto.append(input("digite o produto:"))
    qnt.append(int(input("digite a quantidade:")))
print ("produto")
print (produto)
print ("quantidade:")
print(qnt)
nivel=[]
for valor in qnt:
    if valor<5:
        nivel.append("critico")
    elif (valor>=5 and valor <=10):
        nivel.append("baixo")
    else:
        nivel.append("normal")
for x in range (3):
    print (f"{produto [x]} - {qnt[x]}-{nivel[x]}")