#Elaborar um programa que contém uma lista com N elementos. Essa lista  
#deve ser preenchida pelo usuário e só deve conter números inteiros positivos e  
#pares. Caso o usuário digite o número 1 a repetição termina. Exibir no final todos  
#os elementos da lista. (utilizar while) 

num = []
n = int(input('diga um numero: '))
while (n != -1):
    if n % 2 == 0:
        num.append(n)
    n = int(input('diga um numero: '))
print("estes sao os numero", num)



 
