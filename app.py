import tkinter as interface
from tkinter import *
from tkinter import ttk
from mainSearch import mainSearch
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

menu = interface.Tk()

# Reagentes iniciais disponíveis para seleção
choicesorig = [
    'ETANOL',           # Álcool que pode ser usado como reagente
    'ACIDO_ACETICO',    # Ácido que pode ser usado como reagente  
    'ACIDO_SULFURICO',  # Catalisador que pode ser usado como reagente
    'ETANOL+ACIDO_ACETICO'  # Combinação inicial de reagentes
]

# Produtos finais que podem ser produzidos
choicesobj = [
    'ACETATO_ETILA',    # Éster produzido a partir de etanol e ácido acético
    'POLIESTIRENO'      # Plástico produzido via polimerização
]

# Algoritmos de busca para encontrar rotas químicas
choicesmet = [
    'AMPLITUDE',               # Busca em largura - explora por níveis
    'PROFUNDIDADE',            # Busca em profundidade - explora ramos
    'PROFUNDIDADE_LIMITADA',   # Busca em profundidade com limite
    'APROFUNDAMENTO_ITERATIVO', # Busca que aumenta limite gradualmente
    'BIDIRECIONAL'             # Busca simultânea do início e fim
]

class Application():
    def __init__(self):
        self.menu = menu
        self.tela() # configurações da tela
        #self.frames()
        self.combobox() # caixas de seleção
        self.botoes() # botões de calcular
        self.label_resultado() #label resultado - rodapé
        self.resultado()
        #self.valorcusto()
        menu.mainloop()

    def tela(self):
        self.menu.title("Cálculo de caminho ponderado")
        self.menu.iconbitmap("icone.ico")
        self.menu.geometry("640x480")
        self.menu.configure(bg="lightblue")
        self.menu.resizable(False, False)
        self.label = Label(self.menu, text="Sistema de Otimização de Rotas Químicas",
                           bg="lightblue", font=("Arial", 14))
        self.label.pack(pady=15)
        # Frame para o grafo (sem sobreposição branca)
        self.grafo_frame = Frame(self.menu, highlightbackground="blue", highlightthickness=2)
        self.grafo_frame.place(relwidth=0.48, relheight=0.65, relx=0.48, rely=0.1)

    def combobox(self):
        Label(self.menu, text="REAGENTES DISPONÍVEIS:", 
              bg="lightblue", font=("Arial", 10)).place(relx=0.18, rely=0.08)
        self.dropdownini = ttk.Combobox(self.menu, values=choicesorig,
                                        state="readonly", width=20)
        self.dropdownini.place(
            relwidth=0.35, relheight=0.05, relx=0.06, rely=0.15)
        self.dropdownini.set("Selecione Reagentes")
        self.dropdownfim = ttk.Combobox(self.menu, values=choicesobj,
                                        state="readonly", width=20)
        self.dropdownfim.place(
            relwidth=0.35, relheight=0.05, relx=0.06, rely=0.23)
        self.dropdownfim.set("Selecione Produto")
        self.dropdownmet = ttk.Combobox(self.menu, values=choicesmet,
                                        state="readonly", width=20)
        self.dropdownmet.place(
            relwidth=0.35, relheight=0.05, relx=0.06, rely=0.31)
        self.dropdownmet.set("Selecione Método")
        

    def botoes(self):
        self.btcalc = Button(self.menu, text="ROTA QUÍMICA",
                             width=20, bg="green", fg="white", command=self.valororig)
        self.btcalc.config(font=("Arial", 12, "bold"))
        self.btcalc.place(
            relwidth=0.25, relheight=0.10, relx=0.16, rely=0.4)
        self.btcalc.config(state=NORMAL)

    def label_resultado(self):
        self.labelresultado = Label(self.menu, text="CAMINHO:", bg="lightblue", font=("Arial", 12), border=10)
        self.labelresultado.place(relwidth=0.25, relheight=0.05, relx=-0.04, rely=0.75)
        self.labelresultado.config(state=NORMAL)

    def valororig(self):
        self.resultado.configure(state="normal")
        self.resultado.delete("1.0", END)
        origem = self.dropdownini.get()
        destino = self.dropdownfim.get()
        calculo = self.dropdownmet.get()
        mostra = mainSearch(self, origem, destino, calculo)
        comseta = ' -> '.join(str(valor) for valor in mostra) # só aparece entre os elementos
        print(comseta)
        self.resultado.insert("1.0", comseta)
        self.resultado.configure(state="disable")

        # --- GRAFO NO FRAME (igual ao testeGraphDestaque.py) ---
        # Remove canvas anterior se existir
        if hasattr(self, 'grafo_canvas') and self.grafo_canvas:
            self.grafo_canvas.get_tk_widget().destroy()
            self.grafo_canvas = None

        import os
        if os.path.exists("sourcelist.json"):
            with open("sourcelist.json", "r", encoding="utf-8") as f:
                linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
            cidades = linhas[0].split(',')
            conexoes = [linha.split(',') for linha in linhas[1:]]
            G = nx.Graph()
            for cidade in cidades:
                G.add_node(cidade)
            for i, vizinhos in enumerate(conexoes):
                origem_cid = cidades[i]
                for destino_cid in vizinhos:
                    G.add_edge(origem_cid, destino_cid)

            valores = list(mostra) if isinstance(mostra, (list, tuple)) else []
            node_colors = ['orange' if n in valores else 'lightgray' for n in G.nodes]

            fig, ax = plt.subplots(figsize=(8, 6))
            pos = nx.spring_layout(G, seed=42)
            nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=10, ax=ax, edge_color='gray')
            if valores:
                nx.draw_networkx_nodes(G, pos, nodelist=valores, node_color='orange', node_size=1200, ax=ax)
            plt.tight_layout()

            self.grafo_canvas = FigureCanvasTkAgg(fig, master=self.grafo_frame)
            self.grafo_canvas.draw()
            self.grafo_canvas.get_tk_widget().pack(expand=True, fill='both')
            plt.close(fig)

    #def valorcusto(self):
        #pass  # Removido o widget de custo, agora o grafo é exibido em self.grafo_frame

    def resultado(self):
        self.resultado = Text(self.menu, height=10, width=50, bd=0, bg="white", highlightbackground="blue", highlightthickness=2)
        self.resultado.configure(takefocus=False,)
        self.resultado.configure(state="disable")
        self.resultado.place(relwidth=0.78, relheight=0.1, relx=0.18, rely=0.77)


    #def frames(self):
        #self.frame1 = Frame(self.menu, bd=4, bg="white", highlightbackground="blue", highlightthickness=2)
        #self.frame1.place(relwidth=0.45, relheight=0.5, relx=0.48, rely=0.1)
        # self.resulta.
 
if __name__ == "__main__":
    Application()
