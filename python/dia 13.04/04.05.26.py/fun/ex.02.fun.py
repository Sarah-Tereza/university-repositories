def soma(n1:int, n2:int):
    resultado=0
    for x in range(n1+1, n2):
        resultado += (x)
    return resultado
    
n1=int(input('digite um numero:'))
n2=int(input('digite um numero:'))

print(soma(n1, n2))
