import geometria

x=input('digite o exercicio:')
while x != 'finalizar':

    if x =='a':
        l=float(input('digite o lado do quadrado:'))
        print(geometria.area(l))
    
    elif x == 'b':
        b=float(input('digite a base do retângulo:'))
        h=float(input('digite a altura do retângulo:'))
        print(geometria.area_retangulo(b, h))

    elif x == 'c':
        r=float(input('digite o raio do circulo:'))
        print(geometria.area_circulo(r))

    elif x == 'd':
        r=float(input('digite o raio do circulo:'))
        print(geometria.perimetro(r))

    elif x == 'e':
        r=float(input('digite o raio do cilindro:'))
        h=float(input('digite a altura do cilindro:'))
        print(geometria.volume(r, h))
        
    x=input('digite o exercicio:')
