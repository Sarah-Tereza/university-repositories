def media(nota1:float, nota2:float, nota3:float, letra:str):
    letra=letra.lower()
    if letra == 'a':
        resultado=(nota1+nota2+nota3)/3
        return resultado
    elif letra == 'p':
        resultado =(nota1*5+nota2*3+nota3*2)/10
        return resultado

def soma(n1:int, n2:int):
    resultado=0
    for x in range(n1+1, n2):
        resultado += (x)
    return resultado

def conta(num:float):
    resultado=0
    for x in range(1, num):
        resultado *= x
    return resultado

def elevado(x:float, n:int):
    resultado=x**n
    return resultado

def ex5(a : float, b : float, c : float):
    resultado = elevado(a**3) + elevado(b**5) +(c)
    return resultado   

def dobro(num:int):
    resultado =  num*2
    return int(resultado)

def pn(n:float):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    elif n>0:
        return 1
    
def fa(n:float):
    farnheit = (9*n +160)/5
    return farnheit
    
def kelvin(n:float):
    resultado=n+273.15
    return resultado

def valores(n1:int, n2:int, opção:str):
    if opção=='adição':
        return (n1+n2)
    elif opção=='multiplicação':
        return (n1*n2)
    elif opção=='subtração':
        return (n1-n2)
    elif opção=='divisão':
        return n1/n2
    elif opção=='raiz':
        import math
        quadrado=(math.sqrt(n1))
        return quadrado
    else:
        return 'operação inválida'
    
def primos(num:int):
    for x in range(2, int(num**0.5)+1):
        if num%x==0:
            return ' não é primo'
        return ' é primo'

def np( n:int):
    for x in range (2, n+1):
        if primos(x):
            print('digite outro numero')
            return x
    