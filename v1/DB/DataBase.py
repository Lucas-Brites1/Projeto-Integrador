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

    def fazerPesquisa(self):
        self.cursor.execute(f"SELECT NOME,ID, EMAIL FROM {self.INFOS["database"]}")
        row = self.cursor.fetchall()
        for l in row:
            print(l)

    def produtoJaCadastrado(self, NOME_PRODUTO_VERIFICAR:str):
        query = f"SELECT * FROM {self.INFOS["table"]} WHERE NOME LIKE %s"
        self.cursor.execute(query, (NOME_PRODUTO_VERIFICAR,))
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False

    def cadastrarProdutoDB(self, NOME_PRODUTO: str, DESCRICAO_PRODUTO: str, PRECO_VENDA_PRODUTO: float):
        input_cadastro=input("Gostaria de cadastrar o produto no banco de dados: [S/N]").upper()[0]
        if input_cadastro == "S": 
            if self.produtoJaCadastrado(NOME_PRODUTO_VERIFICAR=NOME_PRODUTO):
                print(f"{NOME_PRODUTO} já está cadastrado no banco de dados!")
                return
            else:
                query= f"INSERT INTO {self.INFOS["table"]} (NOME, DESCRICAO, PRECO) VALUES (%s, %s, %s)"
                values = (NOME_PRODUTO, DESCRICAO_PRODUTO, PRECO_VENDA_PRODUTO)
                self.cursor.execute(query, values)
                self.DB.commit()
                print(f"PRODUTO: {NOME_PRODUTO} cadastrado no banco de dados.")
                return
            
        return None
        
db = DATABASE(PASSWD="@Ninazoemayla32290282", DATABASE="PRODUTOS", TABLE="PRODUTO")
db.produtoJaCadastrado(NOME_PRODUTO_VERIFICAR="teste")


