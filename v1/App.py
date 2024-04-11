from Product import *
from Planilha import GeraradorPlanilha 

def cadastrarProduto(ID, nome, descricao, CP, CF, CV, IV, ML) -> Produto:
    return Produto(ID, nome, descricao, CP, CF, CV, IV , ML)

teste1 = cadastrarProduto(1022, "Testando Produto", "TESTE", 36, 15, 5, 12, 20)
teste1.TABELA()
