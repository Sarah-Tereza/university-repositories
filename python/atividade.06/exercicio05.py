"""
5) Elaborar um programa que contenha a seguinte sequência:
(a) Ler uma string S1 (tamanho mínimo de 20 caracteres, se passar solicitar outra)
(b) Imprimir o tamanho da string S1
(c) Comparar a string S1 com uma nova string S2 (tamanho mínimo de 20 caracteres,
se passar solicitar outra) fornecida pelo usuário e imprimir o resultado da comparação (se é
igual ou não e qual tem a maior quantidade de caracteres)
(d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da
concatenação;
(e) Imprimir a string S1 de forma reversa
(f) Contar quantas vezes um caractere específico aparece na string S1. Esse caractere
deve ser solicitado para o usuário.
(g) Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. Os
caracteres C1 e C2 serão inseridos pelo usuário.
(h) Verificar se uma string S2 é substring (trecho) de S1. A string S2 deve ser informada
pelo usuário.
(i) Retornar uma substring (trecho) da string S1. Para isso o usuário deve informar a
partir de qual posição deve ser criada a substring (trecho) e qual é o tamanho da substring
(trecho)
"""

txt1=input('digite um texto: ')
m=-1
while m<0:
    if len(txt1)>20:
        txt1=input('digite um texto menor: ')
    else:
        print(f'quantidade de caracteres:{len(txt1)}')
        m = m + 2

txt2=input('digite um texto: ')
m=-1
while m<0:
    if len(txt2)>20:
        txt2=input('digite um texto menor: ')
    else:
        print(f'quantidade de caracteres:{len(txt2)}')
        m = m + 2
if txt2 == txt1:
    print('ambas são iguais e possuem o mesmo tamanho!')
else:
    print('são diferentes!')
    if len(txt1) > len(txt2):
        print(f'{txt1} possui mais caracteres que {txt2}')
    elif len(txt1)== len(txt2):
        print('ambas tem a mesma quantidade de caracteres!')
    else:
        print(f'{txt2} tem mais caracteres que {txt1}')

txt2=input('digite um texto: ')
m=-1
while m<0:
    if len(txt2)>20:
        txt2=input('digite um texto menor: ')
    else:
        print(f'concatenação das strings:{txt1 + txt2}')
        m = m + 2
print(f'revertendo a primeira palavra temos:{txt1[::-1]}')

x=input('digite um caractere que deseje verificar: ')
i=0
for letra in txt1:
    if letra == x:
        i = i + 1
print(f'o caractere-{x}- apareceu {i} vezes no primeiro texto')

c1=input('qual caractere deseja substituir?: ')
c2=input('por qual caractere?: ')
txt1_2=""
substituido=False
for caractere in txt1:
    if caractere == c1 and not substituido:
        txt1_2 +=c2
        substituido=True
    else:
        txt1_2 +=caractere
print(f'texto alterado:{txt1_2}')

txt2=input('digite um texto: ')
m=-1
while m<0:
    if len(txt2)>20:
        txt2=input('digite um texto menor: ')
    else:
        m = m + 2
if txt2 in txt1:
    print('o texto inserido é um subtrecho do primeiro')
else:
    print('o texto inserido não é um subtrecho do primeiro')

posição=int(input('escolha de onde começar o subtexto: '))
tamanho=int(input('digite o tamanho que ele terá: '))
substring=txt1[posição: posição+tamanho]
print(substring)
