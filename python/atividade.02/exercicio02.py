'''2) Elaborar um programa que leia a distancia em km e a quantidade de litros de gasolina consumidos por um carro em um percurso,
calcule o consumo em Km/l e mostre uma mensagem de acordo com a tabela abaixo:
consumo        /  km/l  /  mensagem
menor que      /   8    /   venda o carro!
entre          / 8 e 14 /   economico!
maior que      /   12   /   super economico!'''

litro = float(input("digite a litragem gasta: "))
distancia = float(input("digite a distancia percorrida: "))
consumo = distancia / litro
if consumo <= 7:
    print("venda o carro!")
elif consumo >= 8 and consumo <= 14:
    print("economico!")
elif consumo > 12:
    print("super economico!!")
