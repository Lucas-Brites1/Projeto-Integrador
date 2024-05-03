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
        treeFrame = ttk.Frame(self.frame)
        treeFrame.pack(pady=10)
        
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        
        cols=("ID", "Nome do Produto", "Preço de Venda")
        self.treeview = ttk.Treeview(treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)
        self.treeview.pack(fill="both", expand=True)

        botao_atualizar = ttk.Button(self.root, text="Atualizar Tabela", command=self.atualizarTabela)
        botao_atualizar.pack(expand=True, fill="both", pady=10, padx=10)
        
        treeScroll.config(command=self.treeview.yview)

        for col in cols:
            self.treeview.heading(col, text=col, anchor="center")
            self.treeview.column(col, anchor="center")

        for produto in PRODUTOS:
            self.treeview.insert("", tk.END, values=produto)

    def atualizarTabela(self):
        produtos_atualizados = DB.db.fazerPesquisa()

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for produto in produtos_atualizados:
            self.treeview.insert("", tk.END, values=produto)
        
