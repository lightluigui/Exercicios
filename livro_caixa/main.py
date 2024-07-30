import openpyxl
from openpyxl.styles import Font


# Função para criar uma nova planilha de livro caixa
def criar_livro_caixa(nome_arquivo):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Livro Caixa"

    # Cabeçalhos
    headers = ["Data", "Descrição", "Entrada", "Saída", "Saldo"]
    for col_num, header in enumerate(headers, 1):
        cell = sheet.cell(row=1, column=col_num, value=header)
        cell.font = Font(bold=True)

    workbook.save(nome_arquivo)


# Função para adicionar um registro ao livro caixa
def adicionar_registro(nome_arquivo, data, descricao, entrada, saida):
    workbook = openpyxl.load_workbook(nome_arquivo)
    sheet = workbook["Livro Caixa"]

    # Encontrar a próxima linha vazia
    next_row = sheet.max_row + 1

    # Calcular o saldo
    if next_row == 2:  # Se for a primeira linha de dados, não há saldo anterior
        saldo_anterior = 0.0
    else:
        saldo_anterior = sheet.cell(row=next_row - 1, column=5).value
        if saldo_anterior is None:
            saldo_anterior = 0.0
        else:
            saldo_anterior = float(saldo_anterior)

    saldo_atual = saldo_anterior + entrada - saida

    # Adicionar os valores na planilha
    sheet.cell(row=next_row, column=1, value=data)
    sheet.cell(row=next_row, column=2, value=descricao)
    sheet.cell(row=next_row, column=3, value=entrada)
    sheet.cell(row=next_row, column=4, value=saida)
    sheet.cell(row=next_row, column=5, value=saldo_atual)

    workbook.save(nome_arquivo)


# Exemplo de uso
nome_arquivo = "livro_caixa.xlsx"
criar_livro_caixa(nome_arquivo)
adicionar_registro(nome_arquivo, "2024-07-30", "Venda de Produto", 1000.0, 0.0)
