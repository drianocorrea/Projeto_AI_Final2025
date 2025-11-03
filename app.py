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
    'Cana_de_Acucar',
    'Milho'
]

# Produtos finais que podem ser produzidos
choicesobj = [
    'Acucar_Cristal',
    'Etanol_Anidro',
    'Etanol_Hidratado',
    'Melaco',
    'Geracao_Eletrica'
]

# Algoritmos de busca para encontrar rotas químicas
choicesmet = [
    'AMPLITUDE',               # Busca em largura - explora por níveis
    'PROFUNDIDADE',            # Busca em profundidade - explora ramos
    'PROFUNDIDADE_LIMITADA',   # Busca em profundidade com limite
    'APROFUNDAMENTO_ITERATIVO',  # Busca que aumenta limite gradualmente
    'BIDIRECIONAL',            # Busca simultânea do início e fim
    'CUSTO_UNIFORME',          # Busca pelo menor custo uniforme
    'GREEDY',                  # Busca gulosa pela melhor escolha local
    'A_ESTRELA',               # Busca A* combinando custo e heurística
    'AIA_ESTRELA'              # Busca A* com aprofundamento iterativo
]


class Application():
    def __init__(self):
        self.menu = menu
        self.tela()  # configurações da tela
        # self.frames()
        self.combobox()  # caixas de seleção
        self.botoes()  # botões de calcular
        self.label_resultado()  # label resultado - rodapé
        self.resultado()
        # self.valorcusto()
        menu.mainloop()

    def tela(self):
        self.menu.title("Cálculo de caminho ponderado")
        self.menu.iconbitmap("icone.ico")
        # Maximiza a janela
        self.menu.state('zoomed')
        self.menu.configure(bg="lightblue")
        self.menu.resizable(True, True)
        self.label = Label(self.menu, text="Sistema de Otimização de Rotas Químicas",
                           bg="lightblue", font=("Arial", 18, "bold"))
        self.label.pack(pady=20)
        # Frame para o grafo (sem sobreposição branca)
        self.grafo_frame = Frame(
            self.menu, highlightbackground="blue", highlightthickness=2)
        self.grafo_frame.place(
            relwidth=0.55, relheight=0.75, relx=0.42, rely=0.1)

    def combobox(self):
        Label(self.menu, text="REAGENTES DISPONÍVEIS:",
              bg="lightblue", font=("Arial", 12, "bold")).place(relx=0.02, rely=0.08)
        self.dropdownini = ttk.Combobox(self.menu, values=choicesorig,
                                        state="readonly", width=30, font=("Arial", 11))
        self.dropdownini.place(
            relwidth=0.35, relheight=0.06, relx=0.03, rely=0.15)
        self.dropdownini.set("Selecione Reagentes")

        Label(self.menu, text="PRODUTOS DISPONÍVEIS:",
              bg="lightblue", font=("Arial", 12, "bold")).place(relx=0.02, rely=0.23)
        self.dropdownfim = ttk.Combobox(self.menu, values=choicesobj,
                                        state="readonly", width=30, font=("Arial", 11))
        self.dropdownfim.place(
            relwidth=0.35, relheight=0.06, relx=0.03, rely=0.30)
        self.dropdownfim.set("Selecione Produto")

        Label(self.menu, text="MÉTODO DE BUSCA:",
              bg="lightblue", font=("Arial", 12, "bold")).place(relx=0.02, rely=0.38)
        self.dropdownmet = ttk.Combobox(self.menu, values=choicesmet,
                                        state="readonly", width=30, font=("Arial", 11))
        self.dropdownmet.place(
            relwidth=0.35, relheight=0.06, relx=0.03, rely=0.45)
        self.dropdownmet.set("Selecione Método")
        self.dropdownmet.bind('<<ComboboxSelected>>', self.on_method_select)

    def botoes(self):
        self.btcalc = Button(self.menu, text="CALCULAR ROTA QUÍMICA",
                             width=25, bg="green", fg="white", command=self.valororig)
        self.btcalc.config(font=("Arial", 12, "bold"))
        self.btcalc.place(
            relwidth=0.30, relheight=0.06, relx=0.03, rely=0.52)
        self.btcalc.config(state=NORMAL)

    def label_resultado(self):
        # Adiciona label e caixa de texto para o limite de profundidade
        self.labellimite = Label(
            self.menu, text="LIMITE:", bg="lightblue", font=("Arial", 12, "bold"), border=10)
        self.labellimite.place(
            relwidth=0.15, relheight=0.05, relx=0.03, rely=0.61)
        self.limite = Text(self.menu, height=1, width=10, bd=0,
                           bg="white", highlightbackground="blue", highlightthickness=2, font=("Arial", 11))
        self.limite.configure(takefocus=True)
        self.limite.configure(state="disable")
        self.limite.place(relwidth=0.15, relheight=0.05,
                          relx=0.18, rely=0.61)

        # Adiciona label e caixa de texto para o custo
        self.labelcusto = Label(
            self.menu, text="CUSTO:", bg="lightblue", font=("Arial", 12, "bold"), border=10)
        self.labelcusto.place(
            relwidth=0.15, relheight=0.05, relx=0.03, rely=0.68)
        self.custo = Text(self.menu, height=1, width=10, bd=0,
                          bg="white", highlightbackground="blue", highlightthickness=2, font=("Arial", 11))
        self.custo.configure(takefocus=False)
        self.custo.configure(state="disable")
        self.custo.place(relwidth=0.15, relheight=0.05,
                         relx=0.18, rely=0.68)

        self.labelresultado = Label(
            self.menu, text="CAMINHO:", bg="lightblue", font=("Arial", 12, "bold"), border=10)
        self.labelresultado.place(
            relwidth=0.15, relheight=0.05, relx=0.03, rely=0.75)
        self.labelresultado.config(state=NORMAL)

    def on_method_select(self, event):
        metodo = self.dropdownmet.get()
        if metodo == "PROFUNDIDADE_LIMITADA":
            self.limite.configure(state="normal")
            self.limite.delete("1.0", END)
            self.limite.insert("1.0", "5")  # valor padrão
        else:
            self.limite.configure(state="disable")
            self.limite.delete("1.0", END)

    def valororig(self):
        try:
            self.resultado.configure(state="normal")
            self.custo.configure(state="normal")
            self.resultado.delete("1.0", END)
            self.custo.delete("1.0", END)

            origem = self.dropdownini.get()
            destino = self.dropdownfim.get()
            calculo = self.dropdownmet.get()

            if origem == "Selecione Reagentes" or destino == "Selecione Produto" or calculo == "Selecione Método":
                self.resultado.insert(
                    "1.0", "Por favor, selecione todas as opções")
                self.custo.insert("1.0", "N/A")
                return

            if origem == "Milho" and destino == "Acucar_Cristal":
                self.resultado.insert(
                    "1.0", "Não é possível produzir Açúcar Cristal a partir do Milho. O Açúcar Cristal só pode ser produzido a partir da Cana de Açúcar.")
                self.custo.insert("1.0", "N/A")
                return

            # Trata diferentes métodos de busca
            if calculo == "PROFUNDIDADE_LIMITADA":
                try:
                    limite = int(self.limite.get("1.0", END).strip())
                    mostra = mainSearch(self, origem, destino, calculo, limite)
                except ValueError:
                    self.resultado.insert(
                        "1.0", "Por favor, insira um número válido para o limite")
                    self.custo.insert("1.0", "N/A")
                    return
            elif calculo in ["GREEDY", "A_ESTRELA", "AIA_ESTRELA"]:
                if calculo == "AIA_ESTRELA":
                    mostra = mainSearch(self, origem, destino, calculo)
                else:
                    mostra = mainSearch(self, origem, destino, calculo)
            else:
                mostra = mainSearch(self, origem, destino, calculo)

            if isinstance(mostra, list):
                # Calcula o custo (número de etapas - 1)
                custo = len(mostra) - 1
                # Formata o caminho com setas
                comseta = ' -> '.join(str(valor) for valor in mostra)
                print(comseta)
                self.resultado.insert("1.0", comseta)
                self.custo.insert("1.0", str(custo) + " etapas")

                # Atualiza o grafo
                if hasattr(self, 'grafo_canvas') and self.grafo_canvas:
                    self.grafo_canvas.get_tk_widget().destroy()
                    self.grafo_canvas = None

                import os
                if os.path.exists("sourcelist.json"):
                    with open("sourcelist.json", "r", encoding="utf-8") as f:
                        linhas = [linha.strip()
                                  for linha in f.readlines() if linha.strip()]
                    cidades = linhas[0].split(',')
                    conexoes = [linha.split(',') for linha in linhas[1:]]
                    G = nx.Graph()
                    for cidade in cidades:
                        if cidade:  # Verifica se não é string vazia
                            G.add_node(cidade)
                    for i, vizinhos in enumerate(conexoes):
                        if i < len(cidades):  # Verifica se o índice é válido
                            origem_cid = cidades[i]
                            # Ignora o primeiro item que é a origem
                            for destino_cid in vizinhos[1:]:
                                if destino_cid:  # Verifica se não é string vazia
                                    G.add_edge(origem_cid, destino_cid)

                    valores = list(mostra) if isinstance(
                        mostra, (list, tuple)) else []
                    node_colors = [
                        'orange' if n in valores else 'lightgray' for n in G.nodes]

                    fig, ax = plt.subplots(figsize=(8, 6))
                    # Ajustado para melhor visualização
                    pos = nx.spring_layout(G, k=1, iterations=50)
                    nx.draw(G, pos, with_labels=True, node_color=node_colors,
                            node_size=1000, font_size=8, ax=ax, edge_color='gray',
                            font_weight='bold')
                    if valores:
                        nx.draw_networkx_nodes(G, pos, nodelist=valores,
                                               node_color='orange', node_size=1200, ax=ax)
                    plt.tight_layout()

                    self.grafo_canvas = FigureCanvasTkAgg(
                        fig, master=self.grafo_frame)
                    self.grafo_canvas.draw()
                    self.grafo_canvas.get_tk_widget().pack(expand=True, fill='both')
                    plt.close(fig)
            else:
                # Se não encontrou caminho ou houve erro
                self.resultado.insert("1.0", str(mostra))
                self.custo.insert("1.0", "N/A")
        finally:
            self.resultado.configure(state="disable")
            self.custo.configure(state="disable")

        # Grafo já atualizado acima, não precisa repetir

    # def valorcusto(self):
        # pass  # Removido o widget de custo, agora o grafo é exibido em self.grafo_frame

    def resultado(self):
        self.resultado = Text(self.menu, height=10, width=50, bd=0,
                              bg="white", highlightbackground="blue", highlightthickness=2,
                              font=("Arial", 11))
        self.resultado.configure(takefocus=False,)
        self.resultado.configure(state="disable")
        self.resultado.place(relwidth=0.35, relheight=0.12,
                             relx=0.03, rely=0.82)

    # def frames(self):
        # self.frame1 = Frame(self.menu, bd=4, bg="white", highlightbackground="blue", highlightthickness=2)
        # self.frame1.place(relwidth=0.45, relheight=0.5, relx=0.48, rely=0.1)
        # self.resulta.


if __name__ == "__main__":
    Application()
