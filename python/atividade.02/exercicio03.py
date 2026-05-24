''' 3) Elaborar um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostra qual a classificação dessa pessoa.

Altura         | Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90
-----------------------------------------------------------------
Menor que 1,20 |   A    |             D             |      G
De 1,20 a 1,70 |   B    |             E             |      H
Maior que 1,70 |   C    |             F             |      I
'''
altura = float(input("digite a altura: "))
peso = float(input("digite o peso: "))
if altura <= 1.20:
    if peso <= 60:
        print("A")
    elif peso >= 60 and peso <= 90:
        print("B")
    else:
        print("C")
else:
    if altura > 1.20 and altura <= 1.70:
        if peso <= 60:
            print("D")
        elif peso >= 60 and peso <= 90:
            print("E")
        else:
            print("F")
    else:
        if altura > 1.70:
            if peso <= 60:
                print("G")
            elif peso >= 60 and peso <= 90:
                print("H")
            else:
                print("I")
