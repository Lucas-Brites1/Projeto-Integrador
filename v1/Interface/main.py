import tkinter as tk
from tkinter import ttk
import customtkinter
import sys
import os
current_directory=os.path.dirname(__file__)
parent_directory=os.path.dirname(current_directory)
sys.path.append(parent_directory)
import App
from DB import DataBase as DB
import visualizarProdutos
from time import sleep
import tkinter.messagebox as messagebox

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
        self.btn_produto_opcoes = customtkinter.CTkButton(frameButton, text="Funcionalidades", command=lambda frameToClear=self.buttons_frame: self.menu_metodos_produto(frameToClear), width=50, height=5, font=("Segoe UI", 20))
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
        btn_alterar_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Alterar Informações", width=40, height=4, font=("Segoe UI", 20), command= lambda frameToClear=frame_buttons_menu_produto: self.alterar_informacoes_produto(frameToClear=frameToClear))
        btn_alterar_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 3: Visualizar Produtos
        btn_visualizar_produtos = customtkinter.CTkButton(frame_buttons_menu_produto, text="Visualizar Produtos", width=40, height=4, font=("Segoe UI", 20), command= lambda: self.visualizar_produtos())
        btn_visualizar_produtos.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 4: Deletar Produto
        btn_deletar_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Deletar Produto", width=40, height=4, font=("Segoe UI", 20), command= lambda frameToClear=frame_buttons_menu_produto: self.deletar_produto(frameToClear=frameToClear))
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
        
    def visualizar_produtos(self):
        TABELA_PRODUTOS = visualizarProdutos.TabelaProdutos()
        TABELA_PRODUTOS.gerarTabelaInterface(PRODUTOS=DB.db.fazerPesquisa())
        TABELA_PRODUTOS.root.mainloop()

    def cadastrar_produto(self, frameToDestroyAfterRegisterProduct):
        dados={}
    
        for i, text_area in enumerate(self.text_areas):
            try:
                # Verifica se o campo atual é numérico
                if i in [3, 4, 5, 6, 7]:  # Índices dos campos numéricos
                    dados[self.labels[i]] = float(text_area.get("1.0", "end-1c"))
                else:
                    dados[self.labels[i]] = text_area.get("1.0", "end-1c").strip()
            except ValueError:
                dados[self.labels[i]] = text_area.get("1.0", "end-1c").strip()  # Se a conversão falhar, mantenha a string
        
        App.cadastrarProduto(interface=True, dados_produto=dados)
        self.back_to_default_page(frame=frameToDestroyAfterRegisterProduct)

    def alterar_informacoes_produto(self, frameToClear):
        self.exit_function(frame=frameToClear)
        self.master.geometry("250x175")
        alterar_informacoes_frame = customtkinter.CTkFrame(self.master, width=600, height=600, fg_color="#141414")
        alterar_informacoes_frame.pack()

        busca_parametro_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Insira o Nome ou ID do Produto:")
        busca_parametro_label.pack(expand=True, fill="both")

        busca_parametro_textbox = customtkinter.CTkTextbox(alterar_informacoes_frame, height=2)
        busca_parametro_textbox.pack(expand=True, fill="both", pady=15)

        botao_busca_parametro_banco_de_dados = customtkinter.CTkButton(alterar_informacoes_frame, corner_radius=40, hover=True, hover_color="green", text="Buscar", command=lambda: buscar_produto(), width=100)
        botao_busca_parametro_banco_de_dados.pack(expand=True, fill="both")

        def buscar_produto():
            input_value_busca = busca_parametro_textbox.get("1.0", "end-1c")
            if input_value_busca == "":
                messagebox.showerror("Erro", "Por favor, insira o Nome ou ID do Produto.")
            else:
                produto = DB.db.visualizarProdutos(TAG=input_value_busca)

                busca_parametro_label.destroy()
                busca_parametro_textbox.destroy()
                botao_busca_parametro_banco_de_dados.destroy()
                self.master.geometry("250x450")

                # Cria novos campos para editar as informações do produto
                novo_nome_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Novo Nome do Produto:")
                novo_nome_label.pack(expand=True, fill="both")
                novo_nome_textbox = customtkinter.CTkTextbox(alterar_informacoes_frame, height=2)
                novo_nome_textbox.pack(expand=True, fill="both")
                novo_nome_textbox.insert("1.0", produto[0][1])

                nova_descricao_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Nova Descrição do Produto:")
                nova_descricao_label.pack(expand=True, fill="both")
                nova_descricao_textbox = customtkinter.CTkTextbox(alterar_informacoes_frame, height=2)
                nova_descricao_textbox.pack(expand=True, fill="both")
                nova_descricao_textbox.insert("1.0", produto[0][2])

                novo_preco_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Novo Preço do Produto:")
                novo_preco_label.pack(expand=True, fill="both")
                novo_preco_textbox = customtkinter.CTkTextbox(alterar_informacoes_frame, height=2)
                novo_preco_textbox.pack(expand=True, fill="both")
                novo_preco_textbox.insert("1.0", produto[0][3])

                INPUTS_VALORES = [novo_nome_textbox, nova_descricao_textbox, novo_preco_textbox]

                botao_enviar_alteracoes = customtkinter.CTkButton(alterar_informacoes_frame, text="Enviar", command=lambda: self.enviar_alteracoes_produto(produto, text_boxes=INPUTS_VALORES))
                botao_enviar_alteracoes.pack(expand=True, fill="both", pady=10)

        botao_voltar_menu_produtos = customtkinter.CTkButton(alterar_informacoes_frame, corner_radius=40, hover=True, hover_color="green", text="Voltar ao menu", command=lambda: self.menu_metodos_produto(frameToClear=alterar_informacoes_frame))
        botao_voltar_menu_produtos.pack(expand=True, fill="both", pady=20)

    def enviar_alteracoes_produto(self, produto, text_boxes):
        dados = {
            "NOME": None,
            "DESCRICAO": None,
            "VALOR": None
        }

        for i, valor_input in enumerate(text_boxes):
            if i==0:
                dados["NOME"]=valor_input.get("1.0", "end-1c")
            elif i==1:
                dados["DESCRICAO"]=valor_input.get("1.0", "end-1c")
            else:
                dados["VALOR"]=valor_input.get("1.0", "end-1c")   
        
        DB.db.atualizarProduto(PRODUTO=produto, PRODUTO_ATUALIZADO=dados)

    def deletar_produto(self, frameToClear):
        self.exit_function(frame=frameToClear)

        self.master.geometry("350x200")
        frame_deletar_produto = customtkinter.CTkFrame(self.master, width=200, height=200, fg_color="#141414")
        frame_deletar_produto.pack(expand=True, fill="both")

        customtkinter.CTkLabel(frame_deletar_produto, text="Insira o NOME ou ID do Produto que quer remover: ").pack(expand=True, fill="both")

        texto_input = customtkinter.CTkTextbox(frame_deletar_produto, width=250, height=0.1, corner_radius=4, font=("Segoe UI", 12))
        texto_input.pack(expand=True, fill="both", pady=10)

        def confirmar(input):
            valor = input.get("1.0", "end-1c")
            print(valor)
            if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar o produto?"):
                DB.db.deletarProduto(SEARCH_PARAMETER_TO_DELETE=valor)
                print("Produto deletado com sucesso!")

        botao_confirmar_delecao = customtkinter.CTkButton(frame_deletar_produto, text="Deletar Produto", command= lambda: confirmar(input=texto_input))
        botao_confirmar_delecao.pack(expand=True, fill="both")
        botao_voltar_menu_produtos = customtkinter.CTkButton(frame_deletar_produto, hover=True, hover_color="green", text="Voltar ao menu", command=lambda: self.menu_metodos_produto(frameToClear=frame_deletar_produto))
        botao_voltar_menu_produtos.pack(expand=True, fill="both", pady=20)

def main():

    root = customtkinter.CTk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
