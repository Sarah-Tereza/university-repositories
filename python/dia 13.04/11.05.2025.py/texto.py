def nome(name:str):
    name=name.lower()
    if name[0] == 'a' or name[0] == 'e':
        return name

def atv3(nome:str, nome_inverte:str):
    for letra in nome:
        nome_inverte= letra + nome_inverte
    print(nome_inverte)

def atv4(palavra:str, resultado:str):
    for x in palavra: 
        if x != 'a' and x != 'e' and x !='i' and x != 'o' and x != 'u':
           resultado = resultado + x  
    return resultado

