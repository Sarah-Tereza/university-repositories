'''
5- Elaborar o programa em Python que realiza o cálculo e exiba o imposto de renda a 
ser pago. O programa deve receber o número de dependentes do contribuinte e a renda 
mensal. O imposto de renda é calculado levando em consideração:

- Desconto de R$ 135,00 por cada dependente.
- Renda líquida, ou seja, renda mensal menos o desconto calculado anteriormente.
- Imposto de renda a ser pago pelo contribuinte (Renda Líquida * Alíquota).

Alíquota de contribuição apresentada na tabela abaixo:

Renda líquida                   | Alíquota (%)
----------------------------------------------
Até R$ 1.903,98                 | Isento
De R$ 1.903,99 até R$ 2.826,65  | 7,5
De R$ 2.826,66 até R$ 3.751,05  | 15
De R$ 3.751,06 até R$ 4.664,68  | 22,5
Acima de R$ 4.664,68            | 27,5
'''

rm = float(input("Inserir Renda Mensal: "))
dp = float(input("Inserir Dependentes: "))

d = dp * 189.59
x = rm - d
ri = rm - 135 * dp

if rm <= 1903.98:
    p = 0
    print("Isento")
elif rm >= 1903.99 and rm <= 2826.65:
    print("Aliquota = 7.5%")
    p = 7.5
elif rm >= 2826.66 and rm <= 3751.05:
    print("Aliquota = 15%")
    p = 15
elif rm >= 3751.06 and rm <= 4664.68:
    print("Aliquota = 22.5%")
    p = 22.5
elif rm >= 4664.68:
    print("Aliquota = 27.5%")
    p = 27.5

rl = rm * p / 100
imposto = rm - rl

print("Renda Liquida - (imposto): ")
print("Imposto de renda a ser pago: ", rl)
