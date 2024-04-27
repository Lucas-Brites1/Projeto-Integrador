import tkinter as tk
from tkinter import ttk

class TabelaProdutos():
    def __init__(self):
        self.root = tk.Tk()

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
        treeview = ttk.Treeview(treeFrame, show="headings", columns=cols, height=13, yscrollcommand=treeScroll.set)
        treeview.pack(fill="both", expand=True)
        
        treeScroll.config(command=treeview.yview)

        for col in cols:
            treeview.heading(col, text=col, anchor="center")
            treeview.column(col, anchor="center")

        for produto in PRODUTOS:
            treeview.insert("", tk.END, values=produto)
