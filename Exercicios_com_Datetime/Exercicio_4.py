# Exercício 1 – Contagem regressiva para o fim do ano

#     Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.

from datetime import datetime as dt

now = dt.now()

last_day_of_the_year = dt(2026, 12, 31)

how_many_days_are_left = (last_day_of_the_year - now).days

print(f"Hoje é dia {now.strftime('%d/%m/%Y')} e faltam {how_many_days_are_left} dias para o dia {last_day_of_the_year.strftime('%d/%m/%Y')}")
