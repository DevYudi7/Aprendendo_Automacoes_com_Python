# Exercício 2 – Verificador de evento

#     Peça ao usuário que digite uma data de um evento

#     Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

from datetime import datetime as dt

now = dt.now()

data_digitada = input("Querido usuário, por favor digite a data do evento: ")

data_do_evento = dt.strptime(data_digitada, "%d/%m/%Y")

if now.date() > data_do_evento.date():
    print("Este evento já aconteceu!")
elif now.date() == data_do_evento.date(): 
    print("O evento está acontecendo hoje !")
elif data_do_evento.date() > now.date():
    quantos_dias_faltam = (data_do_evento.date() - now.date()).days
    print(f"Este evento ainda vai acontecer ! e faltam {quantos_dias_faltam} dias para que ele aconteça")
    

