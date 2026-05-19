#01- elaborar um programa para adicionar um novo par de chave-valor ao dicionário, modificar
#um valor xistente e acessar uma chave especifica

dados = {'rainha':'julian','rei':'julian', 'nome':'sandro', 'idade':30, 'cidade':'são paulo', 'estado':'são paulo'}
print(dados)
dados['teste']='iniciar'
print(dados)
dados['nome']='felipe'
print(dados['nome'])

#2 - um programa que mostre todos os pare chave
for chave, valor in dados.items():
    print(chave, valor, sep= ' = ')

#3- verificar se os valores são distintos, se forem iguais iguais apresentar uma mensagem  dizendo q sim, se não, apresentar uma mensagem dizendo q não
valores = list(dados.values())
for k in valores:
    if valores.count(k)>1:
        valores.remove(k)
        print(f'há valores repetidos!, ele é:{k}')


#4renomear uma cahve preservando seu valor sem alterar demais chaves
print(dados.values())
dados['novo teste']=dados.pop('teste')
print(dados)

#5inverter o dicionário trocando suas chaves e valores 
novo={}
for chave, valor in dados.items():
    novo[valor]=chave
print(novo)

#6verificar uma chave escolhida pelo usuário
verificação=input('digite a chave que deseja verificar:')
if verificação in dados.keys():
    print('existe no dicionário' )
    print(verificação, dados[verificação])
else:
    print('não existe')

#7 usuario adicionar uma nova chave e valor 
key=input('digite uma chave:')
vlr=input('digite o valor para a chave:')
dados[key]=vlr
print(dados)
