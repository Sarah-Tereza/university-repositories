'''4-Elaborar um programa em Python que possua uma lista denominada de “lista_A” com 10 elementos e que deve ser preenchida pelo usuário. 
Após isso, o programa deve executar os seguintes passos:  
a) Armazenar em uma variável (simples) a soma entre os valores das posições 3, 4, 6 e 9 da lista e mostrar na tela a soma.  
b) Modificar a posição 8 da lista, atribuindo a esta posição o valor -9.  
c) Mostrar na tela cada valor da lista separados por ‘–‘. '''

lista = []
for i in range(10):
    n = int(input('digite um numero: '))
    lista.append(n)

x = lista[5] + lista[9] - lista[0] - lista[9]
del lista[8]
lista.insert(8, -5)
print(x)
print(lista[0], "-", lista[1], "-", lista[2], "-", lista[3], "-", lista[4], "-", lista[5], "-", lista[6], "-", lista[7], "-", lista[8], "-", lista[9])
