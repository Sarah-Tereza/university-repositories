'''
#elaborar uma funçã qu receba ytes notas de um aluno como paraetros e uma etra.
se a letra for A, a função devera calcular a média aritmética das notas do aluno; se for P,
 devera calcular a média ponderada, co pesos 5,3 e 2
'''
def media(nota1:float, nota2:float, nota3:float, letra:str):
    letra=letra.lower()
    if letra == 'a':
        resultado=(nota1+nota2+nota3)/3
        return resultado
    elif letra == 'p':
        resultado =(nota1*5+nota2*3+nota3*2)/10
        return resultado
    
nota1=float(input('digite um numero:'))
nota2=float(input('digite um numero:'))
nota3=float(input('digite um numero:'))
letra=input('digite um numero:')

print(media(nota1, nota2, nota3, letra))
print(media(10,3,4, 'a'))
print(media(10,10,8,'p'))