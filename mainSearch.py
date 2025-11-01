# from buscaGrafoNP import buscaGrafoNP
from searchPath import searchPath


def Gera_Problema(arquivo):
    f = open(arquivo, "r")

    i = 0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i == 0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1

    return nos, grafo


# PROGRAMA PRINCIPAL
nos, grafo = Gera_Problema("sourcelist.json")

# print("======== Lista de nós ========\n",nos )

result = searchPath()
path = []
"""
origem = input("\nOrigem......: ").upper()
destino = input("Destino.....: ").upper()
metodo = input("Metodo.....: ").upper()
print(metodo)"""
# origem  = "ARAD"
# origem = app.dropdownini.get()
# destino = app.dropdownfim.get()
# destino = "BUCARESTE"

# recebe valor de caixa de seleção de app.py


def mainSearch(self, vem, vai, opcao):
    # vem = self.origem.get()
    # vai = self.destino.get()
    origem = vem
    destino = vai
    metodo = opcao
    limite = 5
    print(metodo)

    if origem not in nos or destino not in nos:
        print("Cidade não está na lista")
    elif metodo == "AMPLITUDE":
        path = result.amplitude(origem, destino, nos, grafo)
        if path != None:
            # caminho = path
            # custo = len(path)-1
            print("\n*****AMPLITUDE*****")
            print("Caminho: ", path)
            print("Custo..: ", len(path)-1)
            return path
        else:
            print("CAMINHO NÃO ENCONTRADO")
    elif metodo == "PROFUNDIDADE":
        path = result.profundidade(origem, destino, nos, grafo)
        if path != None:
            print("\n*****PROFUNDIDADE*****")
            print("Caminho: ", path)
            print("Custo..: ", len(path)-1)
            return path
        else:
            print("CAMINHO NÃO ENCONTRADO")
    elif metodo == "PROFUNDIDADE_LIMITADA":
        path = result.proflimitada(origem, destino, nos, grafo)
        if path != None:
            print("\n*****PROFUNDIDADE LIMITADA*****")
            print("Caminho: ", path)
            print("Custo..: ", len(path)-1)
            return path
        else:
            msgfail = f"NÃO TEM CAMINHO COM O LIMITE DE {limite}"
            print("NÃO TEM CAMINHO COM O LIMITE DE ", limite)
            return msgfail
    elif metodo == "APROFUNDAMENTO_ITERATIVO":
        l_max = len(nos)
        path = result.aprof_iterativo(origem, destino, nos, grafo, l_max)
        if path != None:
            print("\n*****APROFUNDAMENTO ITERATIVO*****")
            print("Caminho: ", path)
            print("Custo..: ", len(path)-1)
            return path
        else:
            print("CAMINHO NÃO ENCONTRADO")
    elif metodo == "BIDIRECIONAL":
        path = result.bidirecional(origem, destino, nos, grafo)
        if path != None:
            print("\n*****BIDIRECIONAL*****")
            print("Caminho: ", path)
            print("Custo..: ", len(path)-1)
            return path
        else:
            print("CAMINHO NÃO ENCONTRADO")
    else:
        print("CAMINHO NÃO ENCONTRADO")




