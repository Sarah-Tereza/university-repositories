"""
2) Elaborar um programa que contém uma lista com 10 elementos. Essa lista deve ser
preenchida pelo usuário. O programa deve ter um sistema de busca que após o usuário
preencher essa lista o programa deve solicitar ao usuário um valor X. O programa deve efetuar
a busca de X na lista. Caso encontre o valor exibir a mensagem "Valor encontrado!" e exibir a
posição do valor na lista, caso contrário exibir "Valor não existe!". Depois disso o programa
deve exibir a mensagem: "Deseja continuar a busca? (s/n)". Se digitar "s" deve solicitar um
novo valor para X, caso contrário termina.
"""

lista = []
for x in range(10):
    lista.append(float(input('digite um numero: ')))

resposta = 's'
while resposta.lower() == 's':
    x = float(input('qual valor deseja achar: '))
    if lista.count(x) > 0:
        print('valor encontrado')
        print(f'posição: {lista.index(x)}')
    else:
        print('valor não existe!')
    resposta = input('deseja continuar a busca?(s/n): ')
