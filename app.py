from os import truncate
from openpyxl import Workbook

wb = Workbook()

# Criação de página
while True:
    nome_pagina = str(input('Nome da página: ')).strip().title()
    wb.create_sheet(nome_pagina)

    while True:
        adicionar_pagina = str(input('Quer adicionar outra página? [S/N]: ')).strip().upper()[0]
        if "S" != adicionar_pagina != "N":
            continue
        else:
            break
    if adicionar_pagina == "N":
        break

print(wb.sheetnames)
            
""" 
# Salvar arquivo
nome_arquivo = str(input("Qual nome deseja salvar seu arquivo: ")).capitalize()
wb.save(nome_arquivo + ".xlsx")
 """