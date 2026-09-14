# Exercício 1 – Criando estrutura de pastas

# Crie a seguinte estrutura:

#     ├──dados/
#     │  ├── entrada/
#     │  └── saida/
#     ├──relatorios/

#     Crie todas as pastas em uma única execução do seu código.

# -------------------------------------------------------------------------------

# Exercício 2 – Criar vários arquivos de exemplo

# Dentro da pasta entrada/, crie 3 arquivos vazios:

#     dados1.txt

#     dados2.txt

#     dados3.txt

#--------------------------------------------------------------------------------

# Exercício 3 – Conferindo e filtrando arquivos .txt

#     Liste todos os arquivos .txt dentro de entrada/.

#     Imprima apenas o nome do arquivo (sem o caminho completo).

#--------------------------------------------------------------------------------

"""
OBS: Eram 3 exercícios em arquivos .py diferentes porém eu resolvi fazer em um único arquivo

"""

from pathlib import Path            # Exercicio 1

pasta_dados = Path("dados")

pasta_dados.mkdir(exist_ok = True)

pasta_entrada = pasta_dados / "Entradas"
pasta_saida =  pasta_dados / "Saidas"      

pasta_entrada.mkdir(exist_ok = True )
pasta_saida.mkdir(exist_ok = True)

#-----------------------------------------------------------

dados1 = pasta_entrada / "dados1.txt"       # Exercicio 2
dados1.touch()                              

dados2 = pasta_entrada / "dados2.txt"
dados2.touch()

dados3 = pasta_entrada / "dados3.txt"
dados3.touch()

# -------------------------------------------------------------

for arquivo in pasta_entrada.iterdir():     # Exercicio 3
    print(arquivo.stem)
    






