from openpyxl import Workbook

def opcao_usario(msg):
    while True:
        opcao = str(input(msg)).strip().upper()[0]
        if "S" != opcao != "N":
            continue
        else:
            return opcao

wb = Workbook()

# Criação de página
while True:
    nome_pagina = str(input('Nome da página: ')).strip().title()
    wb.create_sheet(nome_pagina)

    adicionar_pagina = opcao_usario('Quer adicionar outra página? [S/N]: ')
    if adicionar_pagina == "N":
        break
    
print(wb.sheetnames)

# Escolher pagina para manipular
escolher_pagina = str(input('Qual página deseja manipular: ')).strip().title()
pagina_escolhida = wb[escolher_pagina]


""" 
# Salvar arquivo
nome_arquivo = str(input("Qual nome deseja salvar seu arquivo: ")).capitalize()
wb.save(nome_arquivo + ".xlsx")
 """