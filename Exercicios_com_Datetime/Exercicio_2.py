# Exercício 2 – Quantos meses faltam?

#     Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

#         Hoje é o 4º mês do ano. Ainda faltam 8 meses para terminar o ano!

from datetime import datetime as dt

print("----- Quantos Meses faltam para o ano acabar ? -----")

agora = dt.now()

ano_atual = agora.year
mes_atual = agora.month

calculo_meses_que_faltam = 12 - agora.month


print(f"Ano atual: {ano_atual} ")
print(f"Mês atual: {mes_atual} ")
print(f"Faltam {calculo_meses_que_faltam} meses para que o ano de {ano_atual} acabe !")






