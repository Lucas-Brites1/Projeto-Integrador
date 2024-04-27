from Produto.Product import *
from Planilha import GeraradorPlanilha 
from Validar import inputValidation as VALIDAR
from EntradasProduto import inputs as i
import random as rd
from time import sleep
from DB import DataBase as DB

def cadastrarProduto(interface=False, dados_produto=None) -> Produto:
    random_id = rd.randint(0, 1000000)
    if not interface:
        produto_infos = i.inputs_produto()

        if produto_infos == "CADASTRAR NOVAMENTE":
            cadastrarProduto()
        elif produto_infos is None:
            return print("Não foi possível criar o produto.")


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
    else:
        
        try:
            CP_I = float(dados_produto["Custo do Produto (CP): R$"])
            CF_I = int(dados_produto["Custo Fixo/Adminstrativo (CF): %"])
            CV_I = int(dados_produto["Comissão de Vendas (CV): %"])
            IV_I = int(dados_produto["Impostos (IV): %"])
            ML_I = int(dados_produto["Margem de Lucro (ML): %"])
        except ValueError:
            print("Erro: Os valores dos custos devem ser números.")
            return None

        produto = Produto(ID_PRODUTO=random_id, nome=dados_produto["Nome do Produto"], descrição=dados_produto["Descrição do Produto"], CP=dados_produto["Custo do Produto (CP): R$"], 
                          CF=dados_produto["Custo Fixo/Adminstrativo (CF): %"], CV=dados_produto["Comissão de Vendas (CV): %"], IV=dados_produto["Impostos (IV): %"], ML=dados_produto["Margem de Lucro (ML): %"], CATEGORIA_PRODUTO=dados_produto["Categoria do Produto"])
        
        if VALIDAR.__(produto) not in [None, True]:
            print("[ERRO NO CADASTRO DO PRODUTO]")
            return None
        
    DB.db.cadastrarProdutoDB(NOME_PRODUTO=produto.nome, DESCRICAO_PRODUTO=produto.descricao, PRECO_VENDA_PRODUTO=produto.precoVenda)
    sleep(1.2)
    produto.TABELA()
    return produto

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

