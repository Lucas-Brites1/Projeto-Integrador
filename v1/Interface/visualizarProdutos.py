import tkinter as tk
from tkinter import ttk
from DB import DataBase as DB

class TabelaProdutos():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tabela de Produtos")

        # Importando o tema personalizado
        self.root.call("source", "forest-dark.tcl")

        # Aplicando o tema
        self.style = ttk.Style(self.root)
        self.style.theme_use("forest-dark")

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

    def gerarTabelaInterface(self, PRODUTOS: tuple):
        self.treeFrame = ttk.Frame(self.frame)
        self.treeFrame.pack(pady=10)
        
        treeScroll = ttk.Scrollbar(self.treeFrame)
        treeScroll.pack(side="right", fill="y")
        
        cols=("ID", "Nome do Produto", "Preço de Venda", "Custo Fornecedor", "Custo Fixo", "Comissão", "Imposto", "Margem")
        self.treeview = ttk.Treeview(self.treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)
        self.treeview.pack(fill="both", expand=True)
        
        botao_atualizar = ttk.Button(self.root, text="Atualizar Tabela", command=self.atualizarTabela)
        botao_atualizar.pack(expand=True, fill="both", pady=10, padx=10)
        
        treeScroll.config(command=self.treeview.yview)
        
        for col in cols:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor="center")
        
        for produto in PRODUTOS:
            # Formatando o custo fixo para exibir como "15% R$ 300.50"
            CUSTO_FORNECEDOR = F"R$ {produto[5]} | {produto[4]}%"
            CUSTO_FIXO = F"R$ {produto[7]} | {produto[6]}%"
            COMISSAO = F"R$ {produto[9]} | {produto[8]}%"
            IMPOSTO = F"R$ {produto[11]} | {produto[10]}%"
            MARGEM = F"R$ {produto[13]} | {produto[12]}%"
            # Inserindo os valores na tabela
            self.treeview.insert("", tk.END, values=(produto[0], produto[1], produto[3], CUSTO_FORNECEDOR, CUSTO_FIXO, COMISSAO, IMPOSTO, MARGEM))

    def atualizarTabela(self):
        produtos_atualizados = DB.db.fazerPesquisa()

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for produto in produtos_atualizados:
            CUSTO_FORNECEDOR = F"R$ {produto[5]} | {produto[4]}%"
            CUSTO_FIXO = F"R$ {produto[7]} | {produto[6]}%"
            COMISSAO = F"R$ {produto[9]} | {produto[8]}%"
            IMPOSTO = F"R$ {produto[11]} | {produto[10]}%"
            MARGEM = F"R$ {produto[13]} | {produto[12]}%"
            self.treeview.insert("", tk.END, values=(produto[0], produto[1], produto[3], CUSTO_FORNECEDOR, CUSTO_FIXO, COMISSAO, IMPOSTO, MARGEM))