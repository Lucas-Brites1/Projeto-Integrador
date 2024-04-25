from Produto.Product import *
from Planilha import GeraradorPlanilha 
from Validar import inputValidation as VALIDAR
from EntradasProduto import inputs as i
import random as rd
from Interface import main as INTERFACE
INTERFACE.main()

def cadastrarProduto() -> Produto:
    produto_infos = i.inputs_produto()

    if produto_infos == "CADASTRAR NOVAMENTE":
        cadastrarProduto()
    elif produto_infos is None:
        return print("Não foi possível criar o produto.")

    random_id = rd.randint(0, 1000000)

    # Verifica se os valores são números válidos antes de fazer a conversão
    try:
        CP = float(produto_infos[2])
        CF = int(produto_infos[3])
        CV = int(produto_infos[4])
        IV = int(produto_infos[5])
        ML = int(produto_infos[6])
    except ValueError:
        return None

    # Cria o produto com os valores convertidos
    produto = Produto(ID_PRODUTO=random_id, nome=produto_infos[0], descrição=produto_infos[1], CP=CP, CF=CF, CV=CV, IV=IV, ML=ML, CATEGORIA_PRODUTO=produto_infos[7])

    if VALIDAR.__(produto) not in [None, True]:
        print("[ERRO NO CADASTRO DO PRODUTO]")
        return None

    produto.TABELA()
    return produto

cadastrarProduto()


"""
0. nome
1. Descrição
2. CP
3. CF
4. CV
5. IV
6. ML
7. CATEGORIA
"""

