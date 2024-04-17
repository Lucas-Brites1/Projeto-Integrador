from Product import *
from Planilha import GeraradorPlanilha 
from Validar import inputValidation as VALIDAR

def cadastrarProduto(ID, nome, descricao, CP, CF, CV, IV, ML, CATEGORIA) -> Produto:
    produto = Produto(ID, nome, descricao, CP, CF, CV, IV , ML, CATEGORIA)
    if VALIDAR.__(produto) not in[None, True]:
        print("ERRO PRODUTO")
        return None
    return produto

teste1 = cadastrarProduto(1022, "Testando Produto", "TESTE", 36, 15, 5, 12, 20, "TESTE")
teste1.TABELA()


