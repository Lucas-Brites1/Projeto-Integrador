import tkinter as tk
from tkinter import ttk
import customtkinter
import sys
import os
current_directory=os.path.dirname(__file__)
parent_directory=os.path.dirname(current_directory)
sys.path.append(parent_directory)
import App

class Interface():
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Produtos")
        self.master.config(bg="#141414")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        #Dimensões do programa
        window_width= 465
        window_height = 200

        #Obtendo as dimensões da tela do usuário
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - (window_width - 300)) // 2
        y = (screen_height - (window_height + 500)) // 2
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.buttons_frame = tk.Frame(self.master, bg="#141414")
        self.menu(self.buttons_frame)

    def menu(self, frameButton):
        # 1. Alterações no Produto
        self.btn_produto_opcoes = customtkinter.CTkButton(frameButton, text="Alterar/Cadastrar Produto", command=lambda frameToClear=self.buttons_frame: self.menu_metodos_produto(frameToClear), width=50, height=5, font=("Segoe UI", 20))
        self.btn_produto_opcoes.configure(corner_radius=5, width=20, height=2)
        self.btn_produto_opcoes.pack(expand=True, fill="both", padx=10, pady=10)
        
        # 2.Botão Sair
        self.btn_sair = customtkinter.CTkButton(frameButton, text="Sair", command=self.master.quit, width=20, height=1, font=("Segoe UI", 20))
        self.btn_sair.pack(expand=True, fill="both", padx=10, pady=10)
        self.btn_sair.configure(corner_radius=5, width=20, height=2, hover_color="red")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

    def menu_metodos_produto(self, frameToClear):
        self.exit_function(frame=frameToClear)
        self.master.geometry("450x520")

        #! Criando Botões de alteração do Produto (Cadastro, Alterar Informações, Deletar Produto, Visualizar Produtos)
        #? Botão 1: Cadastro de Produtos !
        frame_buttons_menu_produto = tk.Frame(self.master, bg="#141414")
        btn_cadastro_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Cadastrar Produto", width=40, height=4, command=lambda frameToClear=frame_buttons_menu_produto: self.cadastrando_produto(frameToClear), font=("Segoe UI", 20))
        btn_cadastro_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 2: Alterar Informações x
        btn_alterar_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Alterar Informações", width=40, height=4, font=("Segoe UI", 20))
        btn_alterar_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 3: Visualizar Produtos
        btn_visualizar_produtos = customtkinter.CTkButton(frame_buttons_menu_produto, text="Visualizar Produtos", width=40, height=4, font=("Segoe UI", 20), command= lambda frame=frameToClear: self.visualizar_produtos(frameToClear=frame_buttons_menu_produto))
        btn_visualizar_produtos.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 4: Deletar Produto
        btn_deletar_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Deletar Produto", width=40, height=4, font=("Segoe UI", 20))
        btn_deletar_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #! Botão 5: Voltar
        btn_voltar_menu_principal = customtkinter.CTkButton(frame_buttons_menu_produto, text="Voltar ao Menu", width=40, height=4, command= lambda frame=frameToClear: self.back_to_default_page(frame=frame_buttons_menu_produto), hover=True, hover_color="green", font=("Segoe UI", 20))
        btn_voltar_menu_principal.pack(expand=True, fill="both", padx=10, pady=10)

        frame_buttons_menu_produto.pack(expand=True, fill="both", padx=10, pady=10)

    def exit_function(self, frame):
        frame.destroy()
        self.master.geometry("465x200")

    def back_to_default_page(self, frame):
        self.exit_function(frame)  # Destruir o frame
        self.master.geometry("465x200")

        self.buttons_frame = tk.Frame(self.master, bg="#141414")
        self.menu(self.buttons_frame)  # Recriar os botões principais

    def cadastrando_produto(self, frameToClear):
        self.exit_function(frame=frameToClear)

        # Criando 6 caixas de entrada com rótulos correspondentes
        self.labels = ["Nome do Produto", "Descrição do Produto", "Categoria do Produto", "Custo do Produto (CP): R$", "Custo Fixo/Adminstrativo (CF): %", "Comissão de Vendas (CV): %", "Impostos (IV): %", "Margem de Lucro (ML): %"]

        self.text_areas=[]
        frame = customtkinter.CTkFrame(self.master, width=200, height=200, fg_color="#141414")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.exit_function(self.buttons_frame)

        for label_text in self.labels:

            label = customtkinter.CTkLabel(frame, text=label_text, font=("Segoe UI", 15), width=50, fg_color="#141414")
            label.pack(fill="both", expand=True, pady=(0, 5))

            text_box = customtkinter.CTkTextbox(frame, width=250, height=0.2, corner_radius=4, font=("Segoe UI", 12))
            text_box.pack(fill="both", expand=True, pady=(0, 5))

            self.text_areas.append(text_box)  # Adicionando a área de texto à lista
            
        self.master.geometry("400x800")

        button_send_data = customtkinter.CTkButton(frame, text="Enviar", command=lambda frame=frame: self.cadastrar_produto(frame), corner_radius=5, anchor="center", hover=True, hover_color="green", height=10)
        button_send_data.pack(expand=True, fill="both", padx=10, pady=10)

        button_back = customtkinter.CTkButton(frame, text="Voltar", command=lambda frame=frame: self.menu_metodos_produto(frame), hover=True, hover_color="#FF0000", corner_radius=5, anchor="center", height=10, width=40)
        button_back.pack(expand=True, fill="both", padx=10, pady=10)
        
    def visualizar_produtos(self, frameToClear):
        self.exit_function(frame=frameToClear)
        self.master.geometry("800x800")

        treeFrame = ttk.Frame(self.master)
        treeFrame.pack(expand=True, fill="both")

        produtos_teste = (("tenis", 30.50), ("calça", 20.50), ("chapeu", 35.25))
        infos_cols = ("Produto", "Preço de Venda")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", background="#141414", foreground="white", fieldbackground="#141414", font=("Segoe UI", 16))  # Definindo a cor de fundo, cor do texto e fonte da tabela
        style.configure("Treeview", background="#161616", foreground="white", fieldbackground="#161616", font=("Segoe UI", 12))  # Definindo a cor de fundo, cor do texto e fonte da tabela
        style.map("Treeview", background=[("selected", "#0078d7")])  # Definindo a cor de fundo quando uma linha é selecionada

        treeview = ttk.Treeview(treeFrame, show="headings", columns=infos_cols, height=13)
        treeview.pack(expand=True, fill="both")

        # Definindo as colunas
        for col in infos_cols:
            treeview.heading(col, text=col, anchor="center")
            treeview.column(col, anchor="center")  # Centralizando o texto nas células

        # Adicionando os valores
        for produto in produtos_teste:
            treeview.insert("", tk.END, values=produto, tags=("produto",),)

        # Atualizando o Treeview
        treeview.update_idletasks()


def confirmar_produto(self, event):
    item = event.widget.selection()[0]
    values = event.widget.item(item)["values"]
    if values:  # Verifica se uma linha foi clicada
        nome_produto, preco_venda, _ = values  # Obtém as informações do produto
        # Aqui você pode realizar as ações desejadas com as informações do produto
        print(f"Produto confirmado: {nome_produto} - Preço de venda: R${preco_venda}")


    def cadastrar_produto(self, frameToDestroyAfterRegisterProduct):
        dados={}
    
        for i, text_area in enumerate(self.text_areas):
            try:
                # Verifica se o campo atual é numérico
                if i in [3, 4, 5, 6, 7]:  # Índices dos campos numéricos
                    dados[self.labels[i]] = float(text_area.get("1.0", "end-1c"))
                else:
                    dados[self.labels[i]] = text_area.get("1.0", "end-1c")
            except ValueError:
                dados[self.labels[i]] = text_area.get("1.0", "end-1c")  # Se a conversão falhar, mantenha a string
        
        App.cadastrarProduto(interface=True, dados_produto=dados)
        self.back_to_default_page(frame=frameToDestroyAfterRegisterProduct)

    def alterar_informacoes_produto(self, parametroBusca: dict):
        # busca_por = parametroBusca["PARAMETRO"] # pode ser ID ou NOME
        # valor_busca = vai ser o valor do ID ou o NOME do produto
        # chama a busca do banco de dados por meio dos dois valores acima BUSCAR_BD(busca_por, valor_busca) -> f"SELECT * FROM BD WHERE (ID ou NOME) = {busca_por}"
        return

def main():
    root = customtkinter.CTk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
