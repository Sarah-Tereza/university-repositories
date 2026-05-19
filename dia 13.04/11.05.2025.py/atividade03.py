nome= input('digite o numero :')
nome_inverte=''

def atv3(nome:str, nome_inverte:str):
    for letra in nome:
        nome_inverte= letra +nome_inverte
    print(nome_inverte)

def atv4(palavra:str, resultado:str):
    for x in palavra: 
        if x != 'a' or x != 'e' or x  !='i' or x != 'o' or x != 'u':
           resultado += x
    return resultado