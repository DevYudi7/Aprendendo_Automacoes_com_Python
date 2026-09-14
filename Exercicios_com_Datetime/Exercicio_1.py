# Exercício 1 – Relógio de verificação

# Mostre a hora atual no terminal, mas com a seguinte regra:

#     Se a hora for antes das 12h, imprima: "Bom dia!"

#     Se estiver entre 12h e 18h: "Boa tarde!"

#     Depois disso: "Boa noite!"

from datetime import datetime 

agora = datetime.now()
hora_atual = agora.hour

if hora_atual < 12:
    print("Bom Dia Usuário !")
    
elif hora_atual >= 12 and hora_atual < 18:
    print("Boa Tarde Usuário !")
    
else:
    print("Boa Noite Usuário !")





