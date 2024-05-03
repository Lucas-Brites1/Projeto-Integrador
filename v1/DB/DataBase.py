import mysql.connector as SQL

class DATABASE():
    def __init__(self, PASSWD: str, DATABASE: str, TABLE: str, HOST="localhost", PORT=3306, USER="root", ):
        self.DB = SQL.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWD,
            database=DATABASE
        )

        self.INFOS={"database": DATABASE, "table": TABLE}

        self.cursor = self.DB.cursor()

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
        self.cursor.execute(f"SELECT ID, NOME, PRECO FROM {self.INFOS["table"]}")
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
    def cadastrarProdutoDB(self, NOME_PRODUTO: str, DESCRICAO_PRODUTO: str, PRECO_VENDA_PRODUTO: float):
        #Verifica se já existe o produto no banco de dados ao chamar a função produtoJaCadastrado passando produto como parametro
        if self.produtoJaCadastrado(NOME_PRODUTO_VERIFICAR=NOME_PRODUTO):
                print(f"{NOME_PRODUTO} já está cadastrado no banco de dados!")
                return
        input_cadastro=input("Gostaria de cadastrar o produto no banco de dados: [S/N]").upper()[0]

        if input_cadastro == "S": 
            query= f"INSERT INTO {self.INFOS["table"]} (NOME, DESCRICAO, PRECO) VALUES (%s, %s, %s)"
            values = (NOME_PRODUTO, DESCRICAO_PRODUTO, PRECO_VENDA_PRODUTO)
            self.cursor.execute(query, values)
            self.DB.commit()
            print(f"PRODUTO: {NOME_PRODUTO} cadastrado no banco de dados.")
            return
            
        return None
    
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
            
        NOME_ANTIGO = PRODUTO[0][1]
        DESCRICAO_ANTIGA = PRODUTO[0][2]
        VALOR_ANTIGO = PRODUTO[0][3]

        novo_nome = PRODUTO_ATUALIZADO["NOME"]
        novo_valor = PRODUTO_ATUALIZADO["VALOR"]
        nova_descricao = PRODUTO_ATUALIZADO["DESCRICAO"]

        try:
            query = "UPDATE PRODUTO SET NOME = %s, DESCRICAO = %s, PRECO = %s WHERE NOME = %s AND DESCRICAO = %s AND PRECO = %s"
            valores = (novo_nome, nova_descricao, novo_valor, NOME_ANTIGO, DESCRICAO_ANTIGA, VALOR_ANTIGO)
            self.cursor.execute(query, valores)
            self.DB.commit()
        except Exception as e:
            raise ValueError("Os valores inseridos são inválidos.")
        
        return True

db = DATABASE(PASSWD="@Ninazoemayla32290282", DATABASE="PRODUTOS", TABLE="PRODUTO")

