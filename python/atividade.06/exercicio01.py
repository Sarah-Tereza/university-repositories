"""
1) Elaborar um programa que tenha uma função, dada uma string passada por
parâmetro, diga se ela é um palíndromo ou não (pode ser com ou sem retorno). O usuário deve
digitar a string. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder
ser lida tanto da direita para a esquerda como da esquerda para a direita (Exemplo: ovo, arara).
"""

# Função que verifica o palíndromo
def ati(nome: str, inverte: str):
    for letra in nome:
        inverte = letra + inverte
    if inverte == nome:
        return 'é um palindromo'
    else:
        return 'não é um palindromo'

# Programa principal
import fun

nome = input('digite um nome: ')
inverte = ""

print(fun.ati(nome, inverte))
