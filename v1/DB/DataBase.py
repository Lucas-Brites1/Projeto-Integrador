import mysql.connector as SQL

class DATABASE():
    def __init__(self, PASSWD: str, DATABASE: str, TABLE: str, HOST="localhost", PORT=3306, USER="root"):
        self.DB = SQL.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWD,
            database=DATABASE
        )

        self.INFOS={"database": DATABASE, "table": TABLE}
        self.cursor = self.DB.cursor()
        self.usarBD()

    def usarBD(self):
        QUERY=F"USE {self.INFOS["database"]};"
        self.cursor.execute(QUERY)

    def visualizarProdutos(self, TAG=None):
        try:
            if TAG is not None:
                try:
                    TAG = int(TAG)
                    TAG = str(TAG)
                    query = f"SELECT * FROM {self.INFOS['table']} WHERE ID = %s"
                    self.cursor.execute(query, (TAG, ))
                    produto = self.cursor.fetchall()
                    print(produto)
                    if produto:
                        return produto
                    else:
                        print("Produto não encontrado.")
                        return []
                except:
                    query = f"SELECT * FROM {self.INFOS['table']} WHERE NOME LIKE %s"
                    self.cursor.execute(query, (TAG, ))
                    produto = self.cursor.fetchall()
                    print(produto)
                    if produto:
                        return produto
                    else:
                        print("Produto não encontrado.")
                        return []

            self.cursor.execute(f"SELECT NOME, PRECO FROM {self.INFOS['table']}")
            produtos = self.cursor.fetchall()
            if not produtos:
                print("Nenhum produto encontrado na base de dados.")
            return produtos
        except Exception as ERR:
            print(f"Erro ao visualizar produtos: {ERR}")
            return []

    # Retorna o resultado de todos os produtos cadastrados na ordem = ID - NOME - PRECO DE VENDA
    def fazerPesquisa(self):
        self.cursor.execute(f"SELECT ID, NOME, DESCRICAO, PRECO, CUSTO_PORCENT, CUSTO_REAIS, CUSTO_FIXO_PORCENT, CUSTO_FIXO_REAIS, COMISSAO_PORCENT, COMISSAO_REAIS, IMPOSTO_PORCENT, IMPOSTO_REAIS, MARGEM_LUCRO_PORCENT, MARGEM_LUCRO_REAIS FROM {self.INFOS['table']}")
        result = self.cursor.fetchall()
        return result

    # Verifica se um produto passado como parametro já existe no banco de dados
    def produtoJaCadastrado(self, NOME_PRODUTO_VERIFICAR:str):
        query = f"SELECT * FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
        self.cursor.execute(query, (NOME_PRODUTO_VERIFICAR,))
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False
        
    # Função para cadastrar o produto ao banco de dados
    def cadastrarProdutoDB(self, NOME_PRODUTO: str, DESCRICAO_PRODUTO: str, MARCA_PRODUTO: str, PRECO_VENDA_PRODUTO: float, CUSTO_PRODUTO_PORCENT:str ,CUSTO_PRODUTO_REAIS: float, CUSTO_FIXO_PORCENT: str, CUSTO_FIXO_REAIS: float, COMISSAO_PORCENT: str, COMISSAO_REAIS: float, IMPOSTO_PORCENT: str, IMPOSTO_REAIS: float, MARGEM_LUCRO_PORCENT: str, MARGEM_LUCRO_REAIS: float):
        if self.produtoJaCadastrado(NOME_PRODUTO_VERIFICAR=NOME_PRODUTO):
            print(f"{NOME_PRODUTO} já está cadastrado no banco de dados!")
            return False
        try:
            query = f"INSERT INTO {self.INFOS['table']} (NOME, DESCRICAO, MARCA, PRECO, CUSTO_PORCENT, CUSTO_REAIS, CUSTO_FIXO_PORCENT, CUSTO_FIXO_REAIS, COMISSAO_PORCENT, COMISSAO_REAIS, IMPOSTO_PORCENT, IMPOSTO_REAIS, MARGEM_LUCRO_PORCENT, MARGEM_LUCRO_REAIS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (NOME_PRODUTO, DESCRICAO_PRODUTO, MARCA_PRODUTO, PRECO_VENDA_PRODUTO, CUSTO_PRODUTO_PORCENT, CUSTO_PRODUTO_REAIS, CUSTO_FIXO_PORCENT, CUSTO_FIXO_REAIS, COMISSAO_PORCENT, COMISSAO_REAIS, IMPOSTO_PORCENT, IMPOSTO_REAIS, MARGEM_LUCRO_PORCENT, MARGEM_LUCRO_REAIS)
            self.cursor.execute(query, values)
            self.DB.commit()
            print(f"PRODUTO: {NOME_PRODUTO} cadastrado no banco de dados.")
            return True
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return False
    
    def deletarProduto(self, SEARCH_PARAMETER_TO_DELETE) -> bool:
        SEARCH_PARAMETER_TO_DELETE.strip()
        if not self.visualizarProdutos(SEARCH_PARAMETER_TO_DELETE):
            print(f"Produto '{SEARCH_PARAMETER_TO_DELETE}' não encontrado.")
            return False
        try:
            ID_PRODUTO = int(SEARCH_PARAMETER_TO_DELETE)
            QUERY = F"DELETE FROM {self.INFOS['table']} WHERE ID = %s"
            VALUES = (ID_PRODUTO,)
        except ValueError:
            QUERY = F"DELETE FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
            VALUES = (SEARCH_PARAMETER_TO_DELETE, )

        self.cursor.execute(QUERY, VALUES)
        self.DB.commit()
        print(F"PRODUTO: {SEARCH_PARAMETER_TO_DELETE} excluído com sucesso.")
        return True

    # Função para atualizar valores de um produto cadastrado
    def atualizarProduto(self, PRODUTO, PRODUTO_ATUALIZADO):
        if len(PRODUTO) == 0:
            print("Produto não encontrado!")
            return False
            
        ID = PRODUTO[0][0]

        novo_nome = PRODUTO_ATUALIZADO["NOME_PRODUTO"]
        nova_descricao = PRODUTO_ATUALIZADO["DESCRICAO_PRODUTO"]
        novo_preco = PRODUTO_ATUALIZADO["PRECO_VENDA_PRODUTO"]
        nova_marca = PRODUTO_ATUALIZADO["MARCA_PRODUTO"]
        novo_custo_porcentagem = PRODUTO_ATUALIZADO["CUSTO_PRODUTO_PORCENT"]
        novo_custo_reais = PRODUTO_ATUALIZADO["CUSTO_PRODUTO_REAIS"]
        novo_custo_fixo_porcent = PRODUTO_ATUALIZADO["CUSTO_FIXO_PORCENT"]
        novo_custo_fixo_reais = PRODUTO_ATUALIZADO["CUSTO_FIXO_REAIS"]
        nova_comissao_porcent = PRODUTO_ATUALIZADO["COMISSAO_PORCENT"]
        nova_comissao_reais = PRODUTO_ATUALIZADO["COMISSAO_REAIS"]
        novo_imposto_porcent = PRODUTO_ATUALIZADO["IMPOSTO_PORCENT"]
        novo_imposto_reais = PRODUTO_ATUALIZADO["IMPOSTO_REAIS"]
        nova_margem_lucro_porcent = PRODUTO_ATUALIZADO["MARGEM_LUCRO_PORCENT"]
        nova_margem_lucro_reais = PRODUTO_ATUALIZADO["MARGEM_LUCRO_REAIS"]

        try:
            query = f"UPDATE {self.INFOS['table']} SET NOME = %s, DESCRICAO = %s, PRECO = %s, MARCA = %s,  CUSTO_PORCENT = %s, CUSTO_REAIS = %s, CUSTO_FIXO_PORCENT = %s, CUSTO_FIXO_REAIS = %s, COMISSAO_PORCENT = %s, COMISSAO_REAIS = %s, IMPOSTO_PORCENT = %s, IMPOSTO_REAIS = %s, MARGEM_LUCRO_PORCENT = %s, MARGEM_LUCRO_REAIS = %s WHERE ID = %s"
            valores = (novo_nome, nova_descricao, novo_preco, nova_marca, novo_custo_porcentagem, novo_custo_reais, novo_custo_fixo_porcent, novo_custo_fixo_reais, nova_comissao_porcent, nova_comissao_reais, novo_imposto_porcent, novo_imposto_reais, nova_margem_lucro_porcent, nova_margem_lucro_reais, ID)
            self.cursor.execute(query, valores)
            self.DB.commit()
        except Exception as e:
            raise ValueError("Os valores inseridos são inválidos.")
        
        return True

#Instanciando o banco de dados:
db = DATABASE(PASSWD="@Ninazoemayla32290282", DATABASE="PRODUTOS", TABLE="PRODUTO")

