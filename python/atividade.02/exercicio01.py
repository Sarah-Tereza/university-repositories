'''Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o trabalhador pode ou não se aposentar.
As condições para aposentadoria são: 
• Ter pelo menos 65 anos,  
• Ou ter trabalhado pelo menos 30 anos,  
• ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos'''

idade = float(input("digite a idade:"))
tempo = float(input("digite o tempo de serviço:"))
if idade >= 65 or tempo >= 30:
    print("pode se aposentar")
elif idade >= 60 and tempo >= 25:
    print("pode se aposentar")
else:
    print("não pode se aposentar")
