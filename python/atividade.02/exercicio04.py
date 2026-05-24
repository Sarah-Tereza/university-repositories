"""
4) Um produto vai sofrer aumento de acordo com a tabela abaixo. Elaborar um programa 
que leia o preço antigo, calcule e mostre o preço novo, e mostre uma mensagem em 
função do preço novo (de acordo com a segunda tabela).

PREÇO ANTIGO          | % AUMENTO |   | PREÇO NOVO                     | MENSAGEM
----------------------------------------------------------------------------------
até R$ 50             |    5%     |   | até R$ 80                      | Barato
entre R$ 50 e R$ 100  |   10%     |   | entre R$ 80 e R$ 120 (incl.)   | Normal
acima de R$ 100       |   15%     |   | entre R$ 120 e R$ 200 (incl.)  | Caro

                                  |   | acima de R$ 200                | Muito caro
"""
antigo = int(input("digite o preco antigo: "))

if antigo <= 50:
    valor = antigo * 1.05
    print("o novo preço é", valor)
elif antigo >= 50 and antigo <= 100:
    valor = antigo * 1.10
    print("o novo preço é", valor)
else:
    if antigo > 100:
        valor = antigo * 1.15
        print("o novo preço é", valor)

if valor <= 80:
    print("barato")
elif valor > 80 and valor <= 120:
    print("normal")
elif valor > 120 and valor <= 200:
    print("caro")
elif valor > 200:
    print("muito caro")
