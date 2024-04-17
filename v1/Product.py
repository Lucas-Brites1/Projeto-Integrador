class Produto:
    
    custoFornecedor = 0
    receitaBruta = 0
    INFOS_EXCEL = {}

    def __init__(self, ID_PRODUTO, nome, descrição, CP, CF, CV, IV, ML, CATEGORIA_PRODUTO):
        #Tenho que fazer os valores serem INPUTS e fazer uma classe para verificar os valores do input se for <0 ou == 0 não deverá ser aceito ou se não for um número.
        self.ID = ID_PRODUTO
        self.nome = nome
        self.descricao = descrição
        self.custo_produto = CP
        self.custo_fixo = CF
        self.comissao = CV
        self.impostos = IV
        self.rentabilidade = ML
        self.precoVenda = self.calcularPrecoDeVenda(self.custo_produto, self.custo_fixo, self.comissao, self.impostos, self.rentabilidade)
        self.classificaoLucro = self.verificarClassificacaoLucro(self.rentabilidade)
        self.receitaBruta_procentagem = CF+CV+IV+ML
        self.fornecedor_porcentagem = (1 - (float(self.receitaBruta_procentagem)/100)) * 100
        self.categoria_produto=CATEGORIA_PRODUTO
        

    def calcularPrecoDeVenda(self, CP, CF, CV, IV, ML):
        return CP / (1 - ((CF + CV + IV + ML) / 100))

    def verificarClassificacaoLucro(self, RENTABILIDADE):
        classificacoes = ["Alto", "Lucro médio", "Lucro baixo", "Equilíbrio", "Prejuízo"]
        verificadores = [RENTABILIDADE > 20, 10 < RENTABILIDADE <= 20, 0 < RENTABILIDADE <= 10, RENTABILIDADE == 0, RENTABILIDADE < 0]
        for i in range(len(verificadores)):
            if verificadores[i]:
                return classificacoes[i]
            
    def HELP(self):
        print("Os atributos de produtos disponíveis para serem acessados são:\nID\ndescricao\ncusto_produto\ncusto_fixo\ncomissao\nimpostos\nrentabilidade\nprecoVenda\nclassificaoLucro")

    def mostrarInformacao(self, atributo):
        if hasattr(self, atributo):
            return getattr(self, atributo)
        else:
            return f"Atributo '{atributo}' não existe neste objeto."
        
    def calcularCustoReais(self, porcentagem, PV):
        return "{:.2f}".format((PV * porcentagem )/ 100)
    
    def TABELA(self):
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
        CV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['CV']) / INFORMACOES_PRODUTO['PV'] * 100)
        IV_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['IV']) / INFORMACOES_PRODUTO['PV'] * 100)
        ML_PORCENTAGEM_FORMATADA = "%.1f" % (float(INFORMACOES_PRODUTO['ML']) / INFORMACOES_PRODUTO['PV'] * 100)

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

        nomesColunas = ["Nome", "Preço de Venda", "Custo de Aquisição", "Receita Bruta", "Custo Fixo", "Comissão de Vendas", "Impostos", "Outros Custos", "Rentabilidade"]
        valoresColunas = [self.nome ,PRECO_VENDA_FORMATADO, INFORMACOES_PRODUTO['FORNECEDOR_$'], INFORMACOES_PRODUTO['RB_$'], INFORMACOES_PRODUTO['CF'], INFORMACOES_PRODUTO['CV'], INFORMACOES_PRODUTO['IV'], OUTROS, INFORMACOES_PRODUTO['ML']]
        valoresPorcentagem = ["100%", FORNECEDOR_PORCENTAGEM_FORMATADA+"%", RB_PORCENTAGEM_FORMATADA+"%",CF_PORCENTAGEM_FORMATADA+"%", CV_PORCENTAGEM_FORMATADA+"%", IV_PORCENTAGEM_FORMATADA+"%", f"{OUTROS / INFORMACOES_PRODUTO['PV'] * 100:.2f}%", ML_PORCENTAGEM_FORMATADA+"%"]
        for i in range(0, len(nomesColunas)):
            self.INFOS_EXCEL[f'{nomesColunas[i]}'] = valoresColunas[i]
        
        gerarExcel = input(f"\n\nGostaria de gerar um documento Excel com as informações do produto: {self.nome}? [S/N]\n").upper()
        while gerarExcel != None:
            if gerarExcel.startswith("S"):
                self.TABELA_EXCEL(self.INFOS_EXCEL, nomesColunas, valoresPorcentagem)
                gerarExcel = None
            elif gerarExcel.startswith("N"):
                print("> Obrigado por usar o programa!\n")
                gerarExcel = None
            else:
                print("Comando inválido.")
                gerarExcel = input(f"\n\nGostaria de gerar um documento Excel com as informações do produto: {self.nome}? [S/N]").upper()
       
    def TABELA_EXCEL(self, INFOS_EXCEL, COLUNAS, PORCENTAGENS):
        from Planilha import GeraradorPlanilha
        GeraradorPlanilha.gerarPlanilha(INFOS_EXCEL, COLUNAS, PORCENTAGENS)


