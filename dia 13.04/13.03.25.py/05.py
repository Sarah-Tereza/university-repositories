txt1=input('digite um texto:')
R=-1
while R <0:
    if len(txt1) >20:
        txt1=input('digite um texto menor:')
    else:
        print(f'quantidade de caracteres:{len(txt1)}')
        R += 1

txt2=input('digite um texto:')
R=-1
while R <0:
    if len(txt2) >20:
        txt2=input('digite um texto menor:')
    else:
        print(f'quantidade de caracteres:{len(txt2)}')
        R += 1
if txt2 == txt1:
    print('ambas são iguais e possuem o mesmo tamanho!')
else:
    print('são diferentes!')
    if len(txt1) > len(txt2):
        print(f'{txt1} possui mais caracteres que {txt2}')
    elif len(txt1)< len(txt2):
        print('ambas tem a mesma quantidade de caracteres!')
    else:
        print(f'{txt2} tem mais caracteres que {txt1}')
txt2=input('digite um texto:')
R=-1
while R <0:
    if len(txt2) >20:
        txt2=input('digite um texto menor:')
    else:
        R +=1
print(f'concatenação das strings:{txt1  +txt2}')

print (f'revertendo a primeira palavra temos:{txt1[::-1]}')

x=input('digite um caractere que deseje verificar:')    

i=0
for letra in txt1:
    if letra == x:
        i +=1
print(f'o caractere-{x}- apareceu {i} vezes no primeiro texto')

c1=input('qual caractere deseja substituir?:')
c2=input('por qual caractere?:')
txt1_2=""
substituido=False
for caractere in txt1:
    if caractere == c1 and not substituido:
        txt1_2 +=c2
        substituido=True
    else:
        txt1_2 +=caractere
print(f'texto alterado:{txt1_2}')

txt2=input('digite um texto:')
R=False
while R:
    if len(txt2) >20:
        txt2=input('digite um texto menor:')
    else:
        R =True
if txt2 in txt1:
    print('o texto inserido é um subtrecho do primeiro')
else:
    print('o texto inserido não é um subtrecho do primeiro')

posição=int(input('escolha de onde começar o subtexto:'))
tamanho=int(input('digite o tamanho que ele terá:'))
substring=txt1[posição: posição+tamanho]
print(substring )
