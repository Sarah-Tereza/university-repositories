def conta(num):
    resultado=1
    for x in range(1, num + 1):
        resultado *= x
    return resultado

num=int(input("Inserir número"))
print(conta(num))