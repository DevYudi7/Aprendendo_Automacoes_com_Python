# Exercício 3 – Validade de produto 🥫

# Peça ao usuário para informar a data de fabricação de um produto.
# Considere que ele vence em 180 dias.
# Mostre:

#     A data de validade

#     Se o produto ainda está válido ou já venceu

#     Quantos dias faltam ou há quanto tempo passou do prazo

from datetime import datetime as dt, timedelta

now = dt.now()
hoje = now.date()

data_de_fabricacao_digitada = input("Caro usuário, digite a data de fabricação do produto: ")
data_de_fabricacao = dt.strptime(data_de_fabricacao_digitada, "%d/%m/%Y")
data_do_vencimento = data_de_fabricacao.date() + timedelta(days= 180)

if hoje == data_do_vencimento:
    print("\nO produto vence hoje !")
    print(f"Porque o produto foi fabricado em {data_de_fabricacao.strftime("%d/%m/%Y")} e como o produto leva cerca de 180 dias para vencer, seu vencimento deve acontecer em {data_do_vencimento.strftime("%d/%m/%Y")}que é exatamente hoje !\n")
elif hoje < data_do_vencimento:
    vence_em = (data_do_vencimento - data_de_fabricacao.date()).days
    print(f"\nO produto ainda está dentro do prazo de validade, e ainda faltam {vence_em} dias para que os produto passe do prazo de válidade.")
    print(f"Porque o produto foi fabricado em {data_de_fabricacao.strftime("%d/%m/%Y")} e como o produto leva cerca de 180 dias para vencer, seu vencimento deve acontecer em {data_do_vencimento.strftime("%d/%m/%Y")}\n")
elif hoje > data_do_vencimento:
     print("\nO produto está vencido !")
     print(f"Porque o produto foi fabricado em {data_de_fabricacao.strftime("%d/%m/%Y")} e como o produto leva cerca de 180 dias para vencer, seu vencimento aconteceu em {data_do_vencimento.strftime("%d/%m/%Y")}\n")
    











