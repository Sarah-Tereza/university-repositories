import financeiro

x=int(input('exercicio escolhido(0 encerrar):'))
while x!= 0:
    if x ==1:
        c=float(input('digite a capital inicial:'))
        i=float(input('digite a taxa de juros:'))
        t=float(input('digite o tempo:'))
        print(financeiro.montante(c, i, t))
    elif x==2:
        c=float(input('digite a capital inicial:'))
        i=float(input('digite a taxa de juros:'))
        t=float(input('digite o tempo:'))
        print(financeiro.mf(c,i,t))

    elif x==3:
        vi=float(input('digite o valor inicial:'))
        d=float(input('insira o percental de desconto:'))
        print(financeiro.mfj(vi,d))
    
    elif x==4:
        vi=float(input('digite o valor inicial:'))
        a=float(input('digite o percentual de aumento:'))
        print(financeiro.valor_final(vi,a))

    elif x==5:
        v=float(input('digite o valor total :'))
        n=float(input('quantidade de parcelas:'))
        print(financeiro.financiamento(v,n))

    x=int(input('exercicio escolhido(0 encerrar):'))
    
