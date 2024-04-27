import mysql.connector as SQL

class DATABASE():
    def __init__(self, PASSWD: str, DATABASE: str, TABLE: str, HOST="", PORT=3306, USER="root", ):
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
        if TAG is not None:
            try:
                TAG=int(TAG)
                TAG=str(TAG)
                query = f"SELECT * FROM {self.INFOS["table"]} WHERE ID = %s"
                self.cursor.execute(query, (TAG, ))
                produto = self.cursor.fetchall()
                print(produto)
                return produto
            
            except:
                query = f"SELECT * FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
                self.cursor.execute(query, (TAG, ))
                produto = self.cursor.fetchall()
                print(produto)
                return produto

        self.cursor.execute(f"SELECT NOME, PRECO FROM {self.INFOS["table"]}")
        produtos = self.cursor.fetchall()
        return produtos

    def fazerPesquisa(self):
        self.cursor.execute(f"SELECT ID, NOME, PRECO FROM {self.INFOS["table"]}")
        result = self.cursor.fetchall()
        return result

    def produtoJaCadastrado(self, NOME_PRODUTO_VERIFICAR:str):
        query = f"SELECT * FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
        self.cursor.execute(query, (NOME_PRODUTO_VERIFICAR,))
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def cadastrarProdutoDB(self, NOME_PRODUTO: str, DESCRICAO_PRODUTO: str, PRECO_VENDA_PRODUTO: float):

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
    
    def deletarProduto(self, SEARCH_PARAMETER_TO_DELETE):
        if type(SEARCH_PARAMETER_TO_DELETE) == int:
            ID_PRODUTO = SEARCH_PARAMETER_TO_DELETE
            QUERY_ID = F"DELETE FROM {self.INFOS["table"]} WHERE ID LIKE {ID_PRODUTO}"
            self.cursor.execute(QUERY_ID, (ID_PRODUTO, ))
        else:
            QUERY = F"DELETE FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
            self.cursor.execute(QUERY, (SEARCH_PARAMETER_TO_DELETE, ))
        
        self.DB.commit
        print(F"PRODUTO: {SEARCH_PARAMETER_TO_DELETE} excluído com sucesso.")

    def atualizarProduto(self, SEARCH_PARAMETER_TO_MODIFY):
        return
        
db = DATABASE(PASSWD="@Ninazoemayla32290282", DATABASE="PRODUTOS", TABLE="PRODUTO")
db.produtoJaCadastrado(NOME_PRODUTO_VERIFICAR="teste")


