# 3. Automatizando extração de arquivos

# Considerando o arquivo zip que deixei na sessão de recursos, crie um script que:

#     Crie uma pasta chamada extraido/.

#     Extraia o conteúdo do .zip dentro da pasta criada.

#     Ao final, liste todos os arquivos extraídos.

import shutil

from pathlib import Path

folder_extraido = Path("Extraido")
folder_extraido.mkdir(parents = True, exist_ok = True)

shutil.unpack_archive("arquivos_secretos.zip", "Extraido/")

for arquivo in folder_extraido.iterdir():
    print(arquivo.name)
    



