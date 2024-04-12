from Product import *
from Planilha import GeraradorPlanilha 
from Validar import inputValidation as VALIDAR

def cadastrarProduto(ID, nome, descricao, CP, CF, CV, IV, ML) -> Produto:
    produto = Produto(ID, nome, descricao, CP, CF, CV, IV , ML)
    if VALIDAR.__(produto) not in[None, True]:
        print("ERRO PRODUTO")
        return None
    return produto

teste1 = cadastrarProduto(1022, "Testando Produto", "TESTE", -36, 15, 5, 12, 20)
teste1.TABELA()

teste2 = cadastrarProduto(1, "Samsung Galaxy S24", "Celular de ultima geração", 3800, 8, 3, 12, 30)
teste2.TABELA()

monitor = cadastrarProduto(20020, "Alienware 24GLHF600F", "Monitor 360HZ", 2800, 8, 0, 4, 22)
monitor.TABELA()

