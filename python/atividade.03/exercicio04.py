#Elaborar um programa que contém uma lista com 5 elementos. O usuário deve preencher essa lista. Exibir no final os valores inseridos pelo usuário, porém os  
#valores negativos (caso existirem) devem ser substituídos por zero (0). (utilizar for 

lista = []
for i in range (5):
    n = int(input("digite um numero:"))
    if n < 0:
        lista.append (0)
    else:
        lista.append (n)
print ('esta é a lista de numeros inseridos', lista)
