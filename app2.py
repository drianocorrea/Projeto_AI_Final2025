import tkinter as tk
from tkinter import *
from tkinter import ttk
from mainSearch import mainSearch, nos, grafo
from plot_path import plot_graph

menu = tk.Tk()

choicesorig = ['ARAD', 'BUCARESTE', 'CRAIOVA', 'DOBRETA', 'EFORIE', 'FAGARAS', 'GIORGIU', 'HIRSOVA', 'IASI', 'LUGOJ',
               'MEHADIA', 'NEAMT', 'ORADEA', 'PITESTI', 'RIMNICUVILCEA', 'SIBIU', 'TIMISOARA', 'URZICENI', 'VASLUI', 'ZERIND']
choicesobj = ['ARAD', 'BUCARESTE', 'CRAIOVA', 'DOBRETA', 'EFORIE', 'FAGARAS', 'GIORGIU', 'HIRSOVA', 'IASI', 'LUGOJ',
              'MEHADIA', 'NEAMT', 'ORADEA', 'PITESTI', 'RIMNICUVILCEA', 'SIBIU', 'TIMISOARA', 'URZICENI', 'VASLUI', 'ZERIND']
choicesmet = ['AMPLITUDE', 'PROFUNDIDADE', 'PROFUNDIDADE_LIMITADA',
              'APROFUNDAMENTO_ITERATIVO', 'BIDIRECIONAL', 'CUSTO_UNIFORME', 'GREEDY', 'A_ESTRELA', 'AIA_ESTRELA']


class Application():
    def __init__(self):
        self.menu = menu
        self.tela()
        self.frames()  # colocar o grafo aqui
        self.combobox()
        self.botoes()
        self.label_resultado()
        self.resultado()
        self.valorcusto()
        global nos, grafo
        # Linha 24 do mainSearch.py
        nos, grafo = Gera_Problema("sourcelist.txt")
        menu.mainloop()

    def tela(self):
        self.menu.title("Cálculo de caminho ponderado")
        self.menu.iconbitmap("icone.ico")
        self.menu.geometry("640x480")
        self.menu.configure(bg="lightblue")
        self.menu.resizable(False, False)
        self.label = Label(menu, text="Bem-vindo ao meu aplicativo!",
                           bg="lightblue", font=("Arial", 14))
        self.label.pack(pady=15)

    def combobox(self):
        self.dropdownini = ttk.Combobox(self.menu, values=choicesorig,
                                        state="readonly", width=20)
        self.dropdownini.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.1)
        self.dropdownini.set("Selecione Origem")
        self.dropdownfim = ttk.Combobox(self.menu, values=choicesobj,
                                        state="readonly", width=20)
        self.dropdownfim.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.18)
        self.dropdownfim.set("Selecione Destino")
        self.dropdownmet = ttk.Combobox(self.menu, values=choicesmet,
                                        state="readonly", width=20)
        self.dropdownmet.place(
            relwidth=0.25, relheight=0.05, relx=0.18, rely=0.26)
        self.dropdownmet.set("Selecione Método")

    def botoes(self):
        self.btcalc = Button(self.menu, text="Calcular",
                             width=20, bg="blue", fg="white", command=self.valororig)
        self.btcalc.config(font=("Arial", 12, "bold"))
        self.btcalc.place(
            relwidth=0.25, relheight=0.08, relx=0.18, rely=0.4)
        self.btcalc.config(state="normal")

    def label_resultado(self):  # caixa de baixo
        self.labelresultado = Label(self.menu, text="CAMINHO:",
                                    bg="lightblue", font=("Arial", 12), border=10)
        self.labelresultado.place(
            relwidth=0.25, relheight=0.05, relx=0.02, rely=0.62)

    def frames(self):
        self.fame1 = Frame(self.menu, bd=4, bg="white",
                           highlightbackground="blue", highlightthickness=2)
        self.frame1.place(relwidth=0.45, relheight=0.5, relx=0.48, rely=0.1)
        # self.result.
        # Frame vazio inicial para o gráfico
        self.graph_frame = Frame(self.frame1)
        self.graph_frame.pack(fill=BOTH, expand=True)

    def valororig(self):
        # Linhas 58-62 originais (limpeza dos campos)
        self.custo.configure(state="normal")
        self.custo.delete("1.0", END)
        self.result.configure(state="normal")
        self.result.delete("1.0", END)

        # Linhas 64-66 originais (obtenção dos valores)
        origem = str(self.dropdownini.get()).strip().upper()
        destino = str(self.dropdownfim.get()).strip().upper()
        metodo = self.dropdownmet.get()

        try:
            # Linha 68 original - REMOVER parâmetro 'app' não utilizado
            mostra = mainSearch(origem, destino, metodo)  # Alteração

            # NOVO: Tratamento unificado do retorno (substitui linhas 70-88)
            if mostra is None:
                mostra = "Caminho não encontrado"
            elif not isinstance(mostra, list):
                mostra = str(mostra)

            # Adaptação da plotagem (linhas 72-75 originais)
            if isinstance(mostra, list) and len(mostra) > 0:
                edges = []
                for conexoes in grafo:
                    cidade_origem = conexoes[0]
                    for cidade_destino in conexoes[1:]:
                        # NOVO: Suporte a tuplas (cidade, custo)
                        if isinstance(cidade_destino, tuple):
                            edges.append((cidade_origem, cidade_destino[0]))
                        else:
                            edges.append((cidade_origem, cidade_destino))

                plot_graph(nos, edges, mostra, self.graph_frame)
                caminho_formatado = " → ".join(mostra)
                # Substitui linhas 84-85 originais
                texto_final = f"Caminho: {caminho_formatado}\nCusto: {len(mostra)-1}"
            else:
                texto_final = mostra

        except Exception as e:
            # Substitui o tratamento genérico original
            texto_final = f"Erro ao calcular o caminho: {str(e)}"

        # Linhas 90-103 originais (com ajustes)
        self.result.insert("1.0", texto_final)
        self.custo.insert(
            "1.0", texto_final if "Custo:" not in texto_final else texto_final.split("\n")[1])
        self.result.configure(state="disabled")
        self.custo.configure(state="disabled")

    def valorcusto(self):
        self.custo = Text(self.frame1, width=20, bd=0)
        self.custo.configure(state="disabled")
        # self.custo.insert("1.0","Calcular custo")
        # self.custo.configure(takefocus=False,)  # Disable focus on the Text widget
        self.custo.pack(pady=10, padx=10)

    def resultado(self):
        self.result = Text(self.menu, height=10, width=50, bd=0, bg="white",
                           highlightbackground="blue", highlightthickness=2)
        # Disable focus on the Text widget
        self.result.configure(takefocus=False,)
        self.result.configure(state="disabled")
        # self.result.pack(pady=10, padx=100, fill=BOTH, expand=True)

        """self.result = Text(self.menu, height=10, width=50)
        self.result.insert(mainSearch(self, path))
        self.result.configure(state="disabled")"""
        self.result.place(relwidth=0.75, relheight=0.3,
                          relx=0.18, rely=0.63)


Application()
menu.mainloop()
