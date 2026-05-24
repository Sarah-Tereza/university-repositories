#Elaborar um programa que dada a idade de um nadador, classifica-o em uma das seguintes categorias: 
#superior de 18 anos = adulto
#entre 14 e 18 anos = juvenil B
#entre 11 e 14 anos = juvenil A
#entre 8 e 11 anos = infantil B
#entre 5 e 8 anos = infatil A

idade = float(input(" digite a idade do nadador: "))
if idade >= 18:
    print('adulto')
elif idade >= 14:
    print('juvenil B')
elif idade >= 11:
    print('juvenil A')
elif idade >= 8:
    print('infantil B')
elif idade >= 5:
    print("infantil A")
