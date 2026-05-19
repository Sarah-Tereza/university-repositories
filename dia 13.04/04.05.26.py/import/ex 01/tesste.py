for k in range(10):
    escolha=input('qual ex quer:')
    if escolha =="ex1":
        import ex
        nota1=float(input('digite um numero:'))
        nota2=float(input('digite um numero:'))
        nota3=float(input('digite um numero:'))
        letra=input('digite a para media simples, p para ponderada:')
        print(ex.media(nota1, nota2, nota3, letra))
    elif escolha =="ex2":
        import ex
        n1=int(input('digite um numero:'))
        n2=int(input('digite um numero:'))
        print(ex.soma(n1, n2))
    elif escolha =='ex3':
        import ex
        num=int(input("digite um número:"))
        print(ex.conta(num))
    elif escolha =='ex4':
        import ex
        x=float(input('digite um numero:'))
        n=int(input('digite pelo qual dejesa elevar'))
        print(ex.elevado(x, n))
    
    elif escolha =='ex5':
        import ex
        a=int(input('digite um valor:'))
        b=int(input('digite um valor:'))
        c=int(input('digite um valor:'))
        print(ex.ex5(a,b,c))
    elif escolha =='ex6':
        import ex
        n=int(input('digite um numero:'))
        print(ex.dobro(n))
    elif escolha =='ex7':
        import ex
        n=float(input('digite um numero:'))
        print (ex.pn(n))
    elif escolha =='ex8':
        import ex
        n=float(input('digite a temperatura em Cº:'))
        print(ex.fa(n))
    elif escolha =='ex9':
        import ex
        n=float(input('digite a temperatura em Cº:'))
        print (ex.kelvin(n))
    elif escolha =='ex10':
        import ex
        n1=int(input('digite um numero:'))
        n2=int(input('digite outro numero:'))
        print('operações possiveis: adição, subtração, multiplicação, divisão, raiz')
        opção=input('digite a operação:')
        print (ex.valores(n1,n2,opção))
    elif escolha =='ex11':
        import ex 
        num=int(input('digite um numero inteiro:'))
        print(ex.primos(num))
    elif escolha=='ex12':
        import ex
        n=int(input('digite um numero'))
        print(ex.np(n))