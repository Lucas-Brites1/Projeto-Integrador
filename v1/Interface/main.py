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

        #Dimensões do programa
        window_width= 450
        window_height = 210

        #Obtendo as dimensões da tela do usuário
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.x = (screen_width - (window_width - 300)) // 2
        self.y = (screen_height - (window_height + 500)) // 2
        self.master.geometry(f"{window_width}x{window_height}+{self.x}+{self.y}")

        self.buttons_frame = tk.Frame(self.master)
        self.menu(self.buttons_frame)
        self.master.call("source", "forest-dark.tcl")
        self.style = ttk.Style(self.master)
        self.style.theme_use("forest-dark")

    def menu(self, frameButton):
        self.master.title("Menu")
        # 1. Alterações no Produto
        self.btn_produto_opcoes = customtkinter.CTkButton(frameButton, text="Funcionalidades", command=lambda frameToClear=self.buttons_frame: self.menu_metodos_produto(frameToClear), font=("Segoe UI", 20), width=self.x/2, height=self.y/2)
        self.btn_produto_opcoes.pack(fill="both", expand=True, pady=10)
        
        # 2.Botão Sair
        self.btn_sair = customtkinter.CTkButton(frameButton, text="Sair", command=self.master.quit, font=("Segoe UI", 20), width=self.x/2, height=self.y/2)
        self.btn_sair.pack(fill="both", expand=True)
        self.buttons_frame.pack()

    def menu_metodos_produto(self, frameToClear):
        self.master.title("Menu")
        self.exit_function(frame=frameToClear)
        self.master.geometry("425x525")

        #! Criando Botões de alteração do Produto (Cadastro, Alterar Informações, Deletar Produto, Visualizar Produtos)
        #? Botão 1: Cadastro de Produtos !
        frame_buttons_menu_produto = tk.Frame(self.master, bg="#141414")
        btn_cadastro_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Cadastrar Produto", width=40, height=4, command=lambda frameToClear=frame_buttons_menu_produto: self.cadastrando_produto(frameToClear), font=("Segoe UI", 20))
        btn_cadastro_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 2: Alterar Informações x
        btn_alterar_produto = customtkinter.CTkButton(frame_buttons_menu_produto, text="Alterar Informações", width=40, height=4, font=("Segoe UI", 20), command= lambda frameToClear=frame_buttons_menu_produto: self.alterar_informacoes_produto(frameToClear=frameToClear))
        btn_alterar_produto.pack(expand=True, fill="both", padx=10, pady=10)

        #? Botão 3: Visualizar Produtos
        btn_visualizar_produtos = customtkinter.CTkButton(frame_buttons_menu_produto, text="Visualizar Produtos", width=40, height=4, font=("Segoe UI", 20), command= lambda: self.visualizar_produtos(self.gerarTabela()))
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
        self.master.title("Cadastrar Produto")
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

            text_box = customtkinter.CTkEntry(frame, width=250, height=0.2, corner_radius=4, font=("Segoe UI", 12), placeholder_text=label_text)
            text_box.pack(fill="both", expand=True, pady=(0, 5))

            self.text_areas.append(text_box)  # Adicionando a área de texto à lista
            
        self.master.geometry("400x800")

        button_send_data = customtkinter.CTkButton(frame, text="Enviar", command=lambda frame=frame: self.cadastrar_produto(frame), corner_radius=5, anchor="center", hover=True, hover_color="green", height=10)
        button_send_data.pack(expand=True, fill="both", padx=10, pady=10)

        button_back = customtkinter.CTkButton(frame, text="Voltar", command=lambda frame=frame: self.menu_metodos_produto(frame), hover=True, hover_color="#FF0000", corner_radius=5, anchor="center", height=10, width=40)
        button_back.pack(expand=True, fill="both", padx=10, pady=10)

    def visualizar_produtos(self, TABELA):
        TABELA()

    def gerarTabela(self):
        TABELA_PRODUTOS =  visualizarProdutos.TabelaProdutos()
        TABELA_PRODUTOS.gerarTabelaInterface(PRODUTOS=DB.db.fazerPesquisa())
        TABELA_PRODUTOS.root.mainloop()

    def cadastrar_produto(self, frameToDestroyAfterRegisterProduct):
        dados={}
    
        for i, text_area in enumerate(self.text_areas):
            try:
                # Verifica se o campo atual é numérico
                if i in [3, 4, 5, 6, 7]:  # Índices dos campos numéricos
                    dados[self.labels[i]] = float(text_area.get())
                else:
                    dados[self.labels[i]] = text_area.get().strip()
            except ValueError:
                dados[self.labels[i]] = text_area.get().strip()  # Se a conversão falhar, mantenha a string
        
        if App.cadastrarProduto(interface=True, dados_produto=dados, confirmarCadastro=messagebox.askyesno(title="Cadastro", message="Gostaria de cadastrar o produto no banco de dados?")) == False:
            messagebox.showerror("Cadastro Erro", "Erro ao cadastrar produto, tente novamente.")
        self.back_to_default_page(frame=frameToDestroyAfterRegisterProduct)

    def verificarProdutosConfirmacao(self):
        if messagebox.askquestion(title="Mostrar Produtos", message="Gostaria de verificar os Produtos registrados?") == "yes":
            return self.gerarTabela()

    def alterar_informacoes_produto(self, frameToClear):
        self.master.title("Alterar Produto")
        self.exit_function(frame=frameToClear)
        self.master.geometry("350x175")
        alterar_informacoes_frame = customtkinter.CTkFrame(self.master, width=350, height=350, fg_color="#141414")
        alterar_informacoes_frame.pack(expand=True, fill="both")

        busca_parametro_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Insira o Nome ou ID do Produto:")
        busca_parametro_label.pack(expand=True, fill="both")

        busca_parametro_textbox = customtkinter.CTkTextbox(alterar_informacoes_frame, width=200, height=30)
        busca_parametro_textbox.pack(expand=True, fill="both")

        botao_busca_parametro_banco_de_dados = customtkinter.CTkButton(alterar_informacoes_frame, corner_radius=10, hover=True, hover_color="green", text="Buscar", command=lambda: buscar_produto(), width=150)
        botao_busca_parametro_banco_de_dados.pack(expand=True, fill="x", pady=5)

        def buscar_produto():
            input_value_busca = busca_parametro_textbox.get("1.0", "end-1c")
            if input_value_busca == "":
                messagebox.showerror("Erro", "Por favor, insira o Nome ou ID do Produto.")
            else:
                produto = DB.db.visualizarProdutos(TAG=input_value_busca)
                if not produto:
                    busca_parametro_textbox.insert("1.0", "Produto não encontrado!\n")
                    sleep(1)
                    messagebox.askretrycancel(title="Tentar novamente!", message=f"Erro ao tentar encontrar produto.\nGostaria de tentar novamente?")
                    self.alterar_informacoes_produto(frameToClear=alterar_informacoes_frame)

                busca_parametro_label.destroy()
                busca_parametro_textbox.destroy()
                botao_busca_parametro_banco_de_dados.destroy()
                self.master.geometry("300x600")

                def mudar_informacoes_valores():
                    if check_var.get() == "on":
                        try:
                            self.exit_function(frame=alterar_informacoes_frame)
                            alterar_informacoes_frame_adicional = customtkinter.CTkFrame(self.master, width=600, height=600, fg_color="#141414")
                            alterar_informacoes_frame_adicional.pack(expand=True, fill="both")
                            self.master.geometry("300x600")
                        
                            labels = ["Nome do Produto", "Descrição do Produto", "Categoria do Produto", "Custo do Produto (CP): R$", "Custo Fixo/Adminstrativo (CF): %", "Comissão de Vendas (CV): %", "Impostos (IV): %", "Margem de Lucro (ML): %"]
                            valores = ["", "", "", produto[0][4] , produto[0][7], produto[0][9], produto[0][11], produto[0][13]]
                            self.input_values = []

                            for i,label_text in enumerate(labels):
                                label = customtkinter.CTkLabel(alterar_informacoes_frame_adicional, text=label_text)
                                label.pack(expand=True, fill="both")
                                if label_text in ["Nome do Produto", "Descrição do Produto", "Categoria do Produto"]:
                                    text_box = customtkinter.CTkEntry(alterar_informacoes_frame_adicional, height=1, placeholder_text=produto[0][i+1])
                                    text_box.insert("end", produto[0][i+1])
                                else:
                                    text_box = customtkinter.CTkEntry(alterar_informacoes_frame_adicional, height=1, placeholder_text=valores[i])
                                text_box.pack(expand=True, fill="both")
                                self.input_values.append(text_box)
                            
                            try:
                                botao_enviar_alteracoes = customtkinter.CTkButton(alterar_informacoes_frame_adicional, text="Enviar", command=lambda: self.enviar_alteracoes_produto_valores(PRODUTO_ENCONTRADO=produto,labels=labels, frame=alterar_informacoes_frame_adicional))
                                botao_enviar_alteracoes.pack(expand=True, fill="both")
                            except Exception as ERR:
                                print(F"ERRO: {ERR}")

                            button_back = customtkinter.CTkButton(alterar_informacoes_frame_adicional, text="Voltar", command=lambda frame=alterar_informacoes_frame_adicional: self.menu_metodos_produto(frame), hover=True, hover_color="#FF0000", corner_radius=5, anchor="center", height=10, width=40)
                            button_back.pack(expand=True, fill="both")
                            return True
                        except Exception as ERR:
                            print(F"Erro ao tentar alterar valores do produto: {ERR}")
                        
                check_var = customtkinter.StringVar(value="off")    
                checkbox = customtkinter.CTkCheckBox(alterar_informacoes_frame, text="Recalcular Valores", variable=check_var, onvalue="on", offvalue="off", command=mudar_informacoes_valores, checkbox_width=25, checkbox_height=25,corner_radius=20)
                checkbox.pack(expand=True)

                novo_nome_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Novo Nome do Produto:")
                novo_nome_label.pack(expand=True, fill="both")
                novo_nome_textbox = customtkinter.CTkEntry(alterar_informacoes_frame, height=1, placeholder_text=produto[0][1])
                novo_nome_textbox.pack(expand=True, fill="both")

                nova_descricao_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Nova Descrição do Produto:")
                nova_descricao_label.pack(expand=True, fill="both")
                nova_descricao_textbox = customtkinter.CTkEntry(alterar_informacoes_frame, height=1, placeholder_text=produto[0][2])
                nova_descricao_textbox.pack(expand=True, fill="both")

                novo_preco_label = customtkinter.CTkLabel(alterar_informacoes_frame, text="Novo Preço do Produto:")
                novo_preco_label.pack(expand=True, fill="both")
                novo_preco_textbox = customtkinter.CTkEntry(alterar_informacoes_frame, height=1, placeholder_text=produto[0][4])
                novo_preco_textbox.pack(expand=True, fill="both")

                INPUTS_VALORES = [novo_nome_textbox, nova_descricao_textbox, novo_preco_textbox]
                botao_enviar_alteracoes = customtkinter.CTkButton(alterar_informacoes_frame, text="Enviar", command=lambda prod=produto: self.enviar_alteracoes_produto(prod, text_boxes=INPUTS_VALORES, frame=alterar_informacoes_frame))
                botao_enviar_alteracoes.pack(expand=True, fill="both", pady=10)

        botao_voltar_menu_produtos = customtkinter.CTkButton(alterar_informacoes_frame, corner_radius=10, hover=True, hover_color="green", text="Voltar ao menu", command=lambda: self.menu_metodos_produto(frameToClear=alterar_informacoes_frame), width=150)
        botao_voltar_menu_produtos.pack(expand=True, fill="x")
        self.verificarProdutosConfirmacao()

    def enviar_alteracoes_produto_valores(self, PRODUTO_ENCONTRADO, labels, frame):
        dados_produto_atualizado = {}
        print(dados_produto_atualizado)

        for i, input in enumerate(self.input_values):
            try:
                # Verifica se o campo atual é numérico
                if i in [3, 4, 5, 6, 7]:  # Índices dos campos numéricos
                    dados_produto_atualizado[labels[i]] = float(input.get())
                else:
                    dados_produto_atualizado[labels[i]] = input.get().strip()
            except ValueError:
                    dados_produto_atualizado[labels[i]] = input.get().strip()  # Se a conversão falhar, mantenha a string

        produto=App.cadastrarProduto(interface=True, dados_produto=dados_produto_atualizado, confirmarCadastro=False)
        
        PRODUTO_ATUALIZADO={
                            "NOME_PRODUTO": produto.nome, 
                            "DESCRICAO_PRODUTO":produto.descricao, 
                            "PRECO_VENDA_PRODUTO":produto.precoVenda, 
                            "CUSTO_PRODUTO_PORCENT": produto.custo_produto_dados[0],
                            "CUSTO_PRODUTO_REAIS": produto.custo_produto_dados[1], 
                            "CUSTO_FIXO_PORCENT":produto.custo_fixo_dados[0], 
                            "CUSTO_FIXO_REAIS":produto.custo_fixo_dados[1], 
                            "COMISSAO_PORCENT":produto.comissao_dados[0], 
                            "COMISSAO_REAIS": produto.comissao_dados[1], 
                            "IMPOSTO_PORCENT":produto.impostos_dados[0],
                            "IMPOSTO_REAIS": produto.impostos_dados[1],
                            "MARGEM_LUCRO_PORCENT": produto.rentabilidade_dados[0], 
                            "MARGEM_LUCRO_REAIS":produto.rentabilidade_dados[1],
                            "MARCA_PRODUTO":produto.categoria_produto
                            }
        
        DB.db.atualizarProduto(PRODUTO=PRODUTO_ENCONTRADO, PRODUTO_ATUALIZADO=PRODUTO_ATUALIZADO)
        self.exit_function(frame=frame)

        self.menu_metodos_produto(frameToClear=frame)
        messagebox.showinfo(title="Alteração bem sucedidade!", message="Alteração de valores bem sucedida!")
        
    def enviar_alteracoes_produto(self, produto, text_boxes, frame):
        
        dados = {
            "NOME": None,
            "DESCRICAO": None,
            "PRECO": None,
            "MARCA": produto[0][3],
            "CUSTO_PORCENT": produto[0][5], 
            "CUSTO_REAIS": produto[0][6],
            "CUSTO_FIXO_PORCENT": produto[0][7],
            "CUSTO_FIXO_REAIS": produto[0][8],
            "COMISSAO_PORCENT": produto[0][9],
            "COMISSAO_REAIS": produto[0][10],
            "IMPOSTO_PORCENT": produto[0][11],
            "IMPOSTO_REAIS": produto[0][12],
            "MARGEM_LUCRO_PORCENT": produto[0][13],
            "MARGEM_LUCRO_REAIS": produto[0][14]
        }

        for i, valor_input in enumerate(text_boxes):
            if i==0:
                dados["NOME"]=valor_input.get("1.0", "end-1c")
            elif i==1:
                dados["DESCRICAO"]=valor_input.get("1.0", "end-1c")
            else:
                dados["PRECO"]=valor_input.get("1.0", "end-1c")   

        try:
            if DB.db.atualizarProduto(PRODUTO=produto, PRODUTO_ATUALIZADO=dados):
                if messagebox.askyesno(title=f"Alterando {dados["NOME"]}", message=f"Confirme a alteração do produto: {dados['NOME']}"):
                    messagebox.showinfo("Alteração", message=F"Alteração do Produto: {dados["NOME"]} concluída.")
                    self.menu_metodos_produto(frameToClear=frame)
            else:
                messagebox.askretrycancel(title="Tentar novamente!", message=f"Erro ao modificar valores do produto, gostaria de tentar novamente?")

        except ValueError as ve:
            messagebox.showerror(title="Erro no Banco de Dados!", message=f"Ocorreu um erro no banco de dados:\n")
            messagebox.askokcancel(title="Valores Inválidos!", message="Algum dos valores inseridos está inválido, por favor, tente novamente.")
            print(F"ERRO ao alterar produto: {ve}")

    def deletar_produto(self, frameToClear):
        self.master.title("Deletar Produto")
        self.exit_function(frame=frameToClear)

        self.master.geometry("350x200")
        frame_deletar_produto = customtkinter.CTkFrame(self.master, width=200, height=200, fg_color="#141414")
        frame_deletar_produto.pack(expand=True, fill="both")

        customtkinter.CTkLabel(frame_deletar_produto, text="Insira o NOME ou ID do Produto que quer remover: ").pack(expand=True, fill="both")

        texto_input = customtkinter.CTkTextbox(frame_deletar_produto, width=250, height=0.1, corner_radius=4, font=("Segoe UI", 12))
        texto_input.pack(expand=True, fill="both", pady=10)

        def confirmar(input):
            valor = input.get("1.0", "end-1c")

            if messagebox.askyesno("Confirmar", "Tem certeza que deseja deletar o produto?"):
                if DB.db.deletarProduto(SEARCH_PARAMETER_TO_DELETE=valor):
                    texto_input.insert("1.0", f" ")
                    sleep(0.7)
                    texto_input.delete("1.0", "end")
                    texto_input.insert("1.0", f"Produto deletado com sucesso!")

        botao_confirmar_delecao = customtkinter.CTkButton(frame_deletar_produto, text="Deletar Produto", command= lambda: confirmar(input=texto_input))
        botao_confirmar_delecao.pack(expand=True, fill="both")
        botao_voltar_menu_produtos = customtkinter.CTkButton(frame_deletar_produto, hover=True, hover_color="green", text="Voltar ao menu", command=lambda: self.menu_metodos_produto(frameToClear=frame_deletar_produto))
        botao_voltar_menu_produtos.pack(expand=True, fill="both", pady=20)
        self.verificarProdutosConfirmacao()

def main():
    root = customtkinter.CTk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
