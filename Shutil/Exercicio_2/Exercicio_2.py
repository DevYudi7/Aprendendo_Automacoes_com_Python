# 2. Mover e renomear arquivos automaticamente

# Crie um script que:

#     Verifica se existe um arquivo chamado relatorio.txt.

#     Move esse arquivo para uma pasta chamada relatorios_antigos.

#     Durante a movimentação, renomeie o arquivo para relatorio_backup.txt.

import shutil

from pathlib import Path

file_relatorio = Path("relatorio.txt")
file_relatorio.touch()

folder_relatorios_antigos = Path("relatorios_antigos")
folder_relatorios_antigos.mkdir(parents = True, exist_ok = True)

if file_relatorio.exists():
    shutil.move("relatorio.txt", "relatorios_antigos/relatorio_backup.txt")
else:
    print("O Arquivo não existe !!!")


