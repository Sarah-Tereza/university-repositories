"""
5) Elaborar um programa para automatizar o caixa de uma lanchonete. Este algoritmo 
deve ler o código do item pedido, a quantidade e calcular o valor a ser pago por aquele 
lanche. No final o programa deve mostrar o total a ser pago. O cardápio da lanchonete é:

CÓDIGO | ESPECIFICAÇÃO   | PREÇO UNITÁRIO (R$)
----------------------------------------------
  100  | Cachorro quente |        3,50
  101  | Bauru simples   |        3,80
  102  | Bauru c/ovo     |        4,50
  103  | Hamburger       |        4,70
  104  | Cheeseburger    |        5,30
  105  | Refrigerante    |        4,00
"""
codigo = input("digite o codigo do produto desejado: ")
quantia = float(input("digite a quantidade: "))

if codigo == '100':
    total = quantia * 3.50
elif codigo == '101':
    total = quantia * 3.80
elif codigo == '102':
    total = quantia * 4.50
elif codigo == '103':
    total = quantia * 4.70
elif codigo == '104':
    total = quantia * 5.30
else:
    if codigo == '105':
        total = quantia * 4
        
print("o valor do seu pedido é: ", total)
