from Produto.Product import *
from Validar import inputValidation as VALIDAR
from EntradasProduto import inputs as i
import random as rd
from time import sleep
from DB import DataBase as DB

def cadastrarProduto(interface=False, dados_produto=None, confirmarCadastro=None) -> Produto:
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
        except ValueError as ERR:
            print(F"Erro ao cadastrar produto: [App.py] -> {ERR}")
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
        
    if confirmarCadastro:
        DB.db.cadastrarProdutoDB(
                                 NOME_PRODUTO=produto.nome, 
                                 DESCRICAO_PRODUTO=produto.descricao, 
                                 PRECO_VENDA_PRODUTO=produto.precoVenda, 
                                 CUSTO_PRODUTO_PORCENT= produto.custo_produto_dados[0], 
                                 CUSTO_PRODUTO_REAIS= produto.custo_produto_dados[1], 
                                 CUSTO_FIXO_PORCENT=produto.custo_fixo_dados[0], 
                                 CUSTO_FIXO_REAIS=produto.custo_fixo_dados[1], 
                                 COMISSAO_PORCENT=produto.comissao_dados[0], 
                                 COMISSAO_REAIS=produto.comissao_dados[1], 
                                 IMPOSTO_PORCENT=produto.impostos_dados[0],
                                 IMPOSTO_REAIS=produto.impostos_dados[1], 
                                 MARGEM_LUCRO_PORCENT=produto.rentabilidade_dados[0], 
                                 MARGEM_LUCRO_REAIS=produto.rentabilidade_dados[1],
                                 MARCA_PRODUTO=produto.categoria_produto
                                 )
    
    return produto

