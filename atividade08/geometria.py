import math

def area(l:float):
   return(f'essa é a área do quadrado:{l**2}')

def area_retangulo(b:float, h:float):
   return(f'essa é a área do retângulo:{b*h}')

def area_circulo(r:float):
   return(f'essa é a área do circulo:{math.pi*(r**2)}')

def perimetro(r:float):
   return(f'essa é a circunferencia do circulo:{2*math.pi*r}')

def volume(r:float, h:float):
   return (f'esse é o volume do cilindro:{math.pi*(r**2)*h}')