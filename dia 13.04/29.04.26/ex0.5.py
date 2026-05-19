usuarios=['teste1', 'teste2', 'teste3']
senhas=['123', '456', '789']

tentativas=0
acesso=False
while tentativas <= 3 and not acesso:
    usuario=input("login:")
    senha=input("senha:")
    if(usuario in usuarios):
        indice=usuarios.index(usuario)
        print(f'essa é o numero da conta:{indice}')
        if(senha==senhas[indice]):
            print('senha e login corretos, acesso concedido')
            acesso = True
        else:
            print('senha errada')
        tentativas=tentativas + 1
    else:
        print('login errado')
    
if not acesso:
    print("acesso negado")
