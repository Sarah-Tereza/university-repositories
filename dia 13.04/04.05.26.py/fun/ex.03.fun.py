'''
elaborar uma função fat que quando chaada retorna o fatorial de um numero, sendo que
esse numero é passado como parametro para a função. Sbendo'''
def conta(num:float):
    resultado=1
    for x in range(1, num + 1):
        resultado *= x
    return resultado

num=int(input("digite um número:"))
print(conta(num))