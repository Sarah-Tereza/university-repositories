pontos=[]
n= float(input('digite a pontuação, digite -1 para encerrar'))
while n != -1:
    pontos.append(n)
    n= float(input('digite a pontuação, digite -1 para encerrar'))
for x in pontos:
    if pontos.count(x)>1:
        pontos.remove(x)
print("pontos unicos",pontos)
pontos.sort()
print ("pontos ordenados",pontos)
pontos.reverse()
print("pontos em ordem decrescente",pontos)

for ponto in range(len(pontos)):
    if ponto<3:
        print(pontos[ponto],'=elite')
    else:
        print(pontos[ponto],'=amadores')