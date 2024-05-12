class Produto:
    def __init__(self, ID_PRODUTO, nome, descrição, CP, CF, CV, IV, ML, CATEGORIA_PRODUTO):
        #Tenho que fazer os valores serem INPUTS e fazer uma classe para verificar os valores do input se for <0 ou == 0 não deverá ser aceito ou se não for um número.
        self.ID = ID_PRODUTO
        self.nome = nome
        self.descricao = descrição
        self.categoria_produto=CATEGORIA_PRODUTO
        self.custo_produto = CP
        self.custo_fixo = int(CF)
        self.comissao = int(CV)
        self.impostos = int(IV)
        self.rentabilidade = int(ML)
        self.precoVenda = self.calcularPrecoDeVenda(self.custo_produto, self.custo_fixo, self.comissao, self.impostos, self.rentabilidade)
        self.receitaBruta_procentagem = CF+CV+IV+ML
        self.fornecedor_porcentagem = (1 - (float(self.receitaBruta_procentagem)/100)) * 100
        self.classificaoLucro = self.verificarClassificacaoLucro(self.rentabilidade)

        self.TABELA(visivel=True)
        
    def calcularPrecoDeVenda(self, CP, CF, CV, IV, ML):
        try:
            return float(CP) / (1 - ((int(CF) + int(CV) + int(IV) + int(ML)) / 100))
        except ZeroDivisionError as ERROR_TYPE:
            print(F"Erro> {ERROR_TYPE}")
            return None

    def verificarClassificacaoLucro(self, RENTABILIDADE):
        classificacoes = ["Alto", "Lucro médio", "Lucro baixo", "Equilíbrio", "Prejuízo"]
        verificadores = [RENTABILIDADE > 20, 10 < RENTABILIDADE <= 20, 0 < RENTABILIDADE <= 10, RENTABILIDADE == 0, RENTABILIDADE < 0]
        for i in range(len(verificadores)):
            if verificadores[i]:
                return classificacoes[i]
            
    def calcularCustoReais(self, porcentagem, PV):
        return "{:.2f}".format((PV * porcentagem )/ 100)
    
    def TABELA(self, visivel=True):
        if not visivel:
            INFORMACOES_PRODUTO = {
                "PV": self.precoVenda,
                "FORNECEDOR_%": self.fornecedor_porcentagem,
                "RB_%": self.receitaBruta_procentagem,
                "FORNECEDOR_$": self.calcularCustoReais(self.fornecedor_porcentagem, self.precoVenda),
                "RB_$": self.calcularCustoReais(self.receitaBruta_procentagem, self.precoVenda),
                "CF": self.calcularCustoReais(self.custo_fixo, self.precoVenda),
                "CV": self.calcularCustoReais(self.comissao, self.precoVenda),
                "IV": self.calcularCustoReais(self.impostos, self.precoVenda),
                "ML": self.calcularCustoReais(self.rentabilidade, self.precoVenda),
            }

            OUTROS = float(INFORMACOES_PRODUTO['CF']) + float(INFORMACOES_PRODUTO["CV"]) + float(INFORMACOES_PRODUTO['IV'])
            REAIS = "R$ "
            PRECO_VENDA_FORMATADO = "{:.2f}".format(INFORMACOES_PRODUTO["PV"])
            FORNECEDOR_PORCENTAGEM_FORMATADA = "%.1f" % INFORMACOES_PRODUTO["FORNECEDOR_%"]
            RB_PORCENTAGEM_FORMATADA = "%.1f" % INFORMACOES_PRODUTO["RB_%"]

            CF_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['CF']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.custo_fixo_dados = [CF_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["CF"]]

            CV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['CV']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.comissao_dados = [CV_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["CV"]]

            IV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['IV']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.impostos_dados = [IV_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["IV"]]

            ML_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['ML']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.rentabilidade_dados = [ML_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["ML"]]
            
        else:
            INFORMACOES_PRODUTO = {
                "PV": self.precoVenda,
                "FORNECEDOR_%": self.fornecedor_porcentagem,
                "RB_%": self.receitaBruta_procentagem,
                "FORNECEDOR_$": self.calcularCustoReais(self.fornecedor_porcentagem, self.precoVenda),
                "RB_$": self.calcularCustoReais(self.receitaBruta_procentagem, self.precoVenda),
                "CF": self.calcularCustoReais(self.custo_fixo, self.precoVenda),
                "CV": self.calcularCustoReais(self.comissao, self.precoVenda),
                "IV": self.calcularCustoReais(self.impostos, self.precoVenda),
                "ML": self.calcularCustoReais(self.rentabilidade, self.precoVenda),
            }

            OUTROS = float(INFORMACOES_PRODUTO['CF']) + float(INFORMACOES_PRODUTO["CV"]) + float(INFORMACOES_PRODUTO['IV'])
            REAIS = "R$ "
            PRECO_VENDA_FORMATADO = "{:.2f}".format(INFORMACOES_PRODUTO["PV"])
            FORNECEDOR_PORCENTAGEM_FORMATADA = "%.1f" % INFORMACOES_PRODUTO["FORNECEDOR_%"]
            RB_PORCENTAGEM_FORMATADA = "%.1f" % INFORMACOES_PRODUTO["RB_%"]

            self.custo_produto_dados = [FORNECEDOR_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO['FORNECEDOR_$']]

            CF_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['CF']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.custo_fixo_dados = [CF_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["CF"]]

            CV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['CV']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.comissao_dados = [CV_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["CV"]]

            IV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['IV']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.impostos_dados = [IV_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["IV"]]

            ML_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['ML']) / INFORMACOES_PRODUTO['PV'] * 100)
            self.rentabilidade_dados = [ML_PORCENTAGEM_FORMATADA, INFORMACOES_PRODUTO["ML"]]

            print("\n=================================================================================================")
            print("Descrição".center(5) + "Valor".center(75) + "%".center(5))
            print("=================================================================================================")
            print(f"A. Preço de Venda: " + f"{(REAIS + PRECO_VENDA_FORMATADO).center(55)}" + "100%".center(25))
            print(f"B. Custo de Aquisição (Fornecedor): {(REAIS + str(INFORMACOES_PRODUTO['FORNECEDOR_$'])).center(21)}" + f"{FORNECEDOR_PORCENTAGEM_FORMATADA}%".center(61))
            print(f"C. Receita Bruta (A-B):" + f"{(REAIS+ str(INFORMACOES_PRODUTO['RB_$'])).center(47)}" + f"{RB_PORCENTAGEM_FORMATADA}%".center(36))
            print(f"D. Custo Fixo/Administrativo:" + f"{(REAIS+ str(INFORMACOES_PRODUTO['CF'])).center(36)}" + f"{CF_PORCENTAGEM_FORMATADA}%".center(45))
            print(f"E. Comissão de Vendas:" + f"{(REAIS+ str(INFORMACOES_PRODUTO['CV'])).center(50)}" + f"{CV_PORCENTAGEM_FORMATADA}%".center(31))
            print(f"F. Impostos:" + f"{(REAIS+ str(INFORMACOES_PRODUTO['IV'])).center(70)}" + f"{IV_PORCENTAGEM_FORMATADA}%".center(12))
            print(f"G. Outros custos (D+E+F):" + f"{(REAIS+ str(OUTROS)).center(43)}" + f"{OUTROS / INFORMACOES_PRODUTO['PV'] * 100:.1f}%".center(39))
            print(f"H. Rentabilidade (C-G):" + f"{(REAIS+ str(INFORMACOES_PRODUTO['ML'])).center(47)}" + f"{ML_PORCENTAGEM_FORMATADA}%".center(36))
            print("------------------------------------------------------------------------------------------------------")