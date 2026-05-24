# Elaborar um programa que lê duas notas (P1 e P2). Caso a médiaj seja maior 
#igual a 5 deve exibir a mensagem “APROVADO”. Caso a média seja menor que  
#5 e maior igual a 3 deve exibir a mensagem “EXAME”. Caso contrário exibir a  
#mensagem “REPROVADO”. Caso esteja de exame o programa deve solicitar a  
#nota de exame e verificar se o aluno está aprovado ou não e exibir o resultado  
#na tela. Esse programa deve-se repetir para 30 alunos. (utilizar for) 

for i in range(1, 31):
    print(f"\nAluno {i}")
    p1 = float(input("Digite a nota da P1: "))
    p2 = float(input("Digite a nota da P2: "))
    
    media = (p1 + p2) / 2
    if media >= 5:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
        exame = float(input("Digite a nota do exame: "))
        
        media_final = (media + exame) / 2
        
        if media_final >= 5:
            print("APROVADO NO EXAME")
        else:
            print("REPROVADO NO EXAME")
    else:
        print("REPROVADO")
