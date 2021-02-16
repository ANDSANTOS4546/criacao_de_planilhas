from openpyxl import Workbook

wb = Workbook()


nome_guia = str(input('Nome da guia: '))

wb.create_sheet(nome_guia)

# Salvar arquivo
wb.save("Teste.xlsx")
