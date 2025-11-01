from tkinter import *
from tkinter import ttk
from valorfunc import *


menu = Tk()

numeros = [1, 2, 3, 4, 5]


class pega:
    def __init__(self):
        self.menu = menu
        # self.tela()
        self.seleciona()
        self.botao()
        self.resultado()
        menu.mainloop()

    def seleciona(self):
        self.opcoes = ttk.Combobox(values=numeros,
                                   state="readonly", width=20)
        self.opcoes.pack()

    def botao(self):
        self.bt = Button(self.menu, text="Calcular",
                         width=20, bg="blue", fg="white", command=self.valor)
        self.bt.config(font=("Arial", 12, "bold"))
        self.bt.pack()
        self.bt.config(state=NORMAL)

    def valor(self):
        v1 = self.opcoes.get()
        # resultado = valorfunc(v1, 2)
        #print(v1)
        #print(sum(v1, 4))
        
        # print(valorfunc(v1, 2))
       
        mostra = compara(v1)
        self.result.configure(state="normal")  # Enable editing temporarily
        self.result.insert("1.0", mostra)
        self.result.configure(state="disable")  # Enable editing temporarily
        
        #print(compara(v1))
    # return v1
    def resultado(self):
        self.result = Text(self.menu, height=10, width=50)
        self.result.pack(pady=10, padx=10, fill=BOTH, expand=True)
       
                          

#print(compara(1))


# print(valorfunc(3, 2))


pega()
