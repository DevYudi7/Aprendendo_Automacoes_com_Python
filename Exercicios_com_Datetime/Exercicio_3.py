# Exercício 3 – Assinatura digital do terminal

#     Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

#         Assinatura gerada por [SEU NOME] em 24 de abril de 2025 às 15:02

#     A data e horário devem ser do momento atual da assinatura

from datetime import datetime as dt

agora = dt.now()

dia_atual = agora.day
mes_atual = agora.strftime("%B")
ano_atual = agora.year
hora_atual = agora.hour
minuto_atual = agora.minute

def Assinatura(nome):
    print(f"Assinatura gerada por {nome} em {dia_atual} de {mes_atual} de {ano_atual} às {hora_atual}:{minuto_atual}")
    
Assinatura("Yudi")
    
