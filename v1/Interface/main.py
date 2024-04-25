import tkinter as tk
import customtkinter
import sys
sys.path.append("C:\\Users\\Lucas\\OneDrive\\Área de Trabalho\\Faculdade-SI\\Projeto-Integrador\\v1")
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
        y = (screen_height - (window_height + 300)) // 2
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.buttons_frame = tk.Frame(self.master, bg="#141414")
        self.construir_opcoes_principais(self.buttons_frame)

    def construir_opcoes_principais(self, frameButton):
        # 1.Botão Cadastrar Produto
        self.btn_cadastrar = customtkinter.CTkButton(frameButton, text="Cadastrar Produto", command=self.abrir_caixas_inputs, width=50, height=5, text_color="#FFFFFF")
        self.btn_cadastrar.configure(corner_radius=5, width=20, height=2)
        self.btn_cadastrar.pack(expand=True, fill="both", padx=10, pady=10)
        
        # 2.Botão Visualizar Produto
        self.btn_visualizar = customtkinter.CTkButton(frameButton, text="Visualizar Produtos", command=self.visualizar_produtos, width=20, height=1)
        self.btn_visualizar.pack(expand=True, fill="both", padx=10, pady=10)
        self.btn_visualizar.configure(corner_radius=5, width=20, height=2)

        # 3.Botão Sair
        self.btn_sair = customtkinter.CTkButton(frameButton, text="Sair", command=self.master.quit, width=20, height=1)
        self.btn_sair.pack(expand=True, fill="both", padx=10, pady=10)
        self.btn_sair.configure(corner_radius=5, width=20, height=2, hover_color="red")
        self.buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

    def exit_function(self, frame):
        frame.destroy()
        self.master.geometry("465x200")

    def back_to_default_page(self, frame):
        self.exit_function(frame)  # Destruir o frame
        self.master.geometry("465x200")

        self.buttons_frame = tk.Frame(self.master, bg="#141414")
        self.construir_opcoes_principais(self.buttons_frame)  # Recriar os botões principais

    def abrir_caixas_inputs(self):
        # Criando 6 caixas de entrada com rótulos correspondentes
        self.labels = ["Nome do Produto", "Descrição do Produto", "Categoria do Produto", "Custo do Produto (CP): R$", "Custo Fixo/Adminstrativo (CF): %", "Comissão de Vendas (CV): %", "Impostos (IV): %", "Margem de Lucro (ML): %"]

        self.text_areas=[]
        frame = customtkinter.CTkFrame(self.master, width=200, height=200)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.exit_function(self.buttons_frame)

        for label_text in self.labels:

            label = customtkinter.CTkLabel(frame, text=label_text, font=("Segoe UI", 15), width=50, fg_color="transparent")
            label.pack(side=tk.TOP, pady=5)

            text_box = customtkinter.CTkTextbox(frame, width=250, height=0.2, corner_radius=4)
            text_box.pack(side=tk.TOP, pady=(0, 5))

            self.text_areas.append(text_box)  # Adicionando a área de texto à lista
            
        self.master.geometry("350x700")

        button_send_data = customtkinter.CTkButton(frame, text="Enviar", command=lambda frame=frame: self.cadastrar_produto(frame), corner_radius=5, anchor="center")
        button_send_data.pack(pady=10)
            
        button_back = customtkinter.CTkButton(frame, text="Voltar", command=lambda frame=frame: self.back_to_default_page(frame), hover=True, hover_color="#FF0000", corner_radius=5, anchor="center")
        button_back.pack(pady=5)

    def visualizar_produtos(self):
        # Função temporária para visualizar produtos
        print("Visualizando produtos...")

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

def main():
    root = customtkinter.CTk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
