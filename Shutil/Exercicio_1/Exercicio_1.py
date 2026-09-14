# 1. Cópia simples com estrutura

# Crie um script que:

#     Crie uma pasta imagens.

#     Coloque 2 arquivos fictícios .png dentro dela

#     Copie todos os arquivos .png da pasta imagens para uma nova pasta chamada backup.

import shutil

from pathlib import Path

path_pasta_img = Path("Imagens")
path_pasta_img.mkdir(exist_ok = True)

arquivo_1 = path_pasta_img / "arquivo_1.png"
arquivo_1.touch()

arquivo_2 = path_pasta_img / "arquivo_2.png"
arquivo_2.touch()

backup = Path("Backup")
backup.mkdir(parents=True, exist_ok = True)

for arquivo in path_pasta_img.iterdir():
    shutil.copy(arquivo, "Backup/")





