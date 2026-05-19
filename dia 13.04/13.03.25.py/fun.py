def at1(nome:str, inverte:str):
    for letra in nome:
        inverte= letra + inverte
    if inverte == nome:
        print ('é um palindromo')
    else:
        print ('não é um palindromo')
    

