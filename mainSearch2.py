# from buscaGrafoNP import buscaGrafoNP
from searchPath import searchPath
from plot_path import plot_graph


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
nos, grafo = Gera_Problema("sourcelist.txt")

result = searchPath()
path = []

# recebe valor de caixa de seleção de app.py
heuristica = {'ARAD': 366, 'BUCARESTE': 0, 'CRAIOVA': 160, 'DOBRETA': 242, 'EFORIE': 161,
              'FAGARAS': 176, 'GIORGIU': 77, 'HIRSOVA': 151, 'IASI': 226, 'LUGOJ': 244, 'MEHADIA': 241, 'NEAMT': 234, 'ORADEA': 380,
              'PITESTI': 100, 'RIMNICUVILCEA': 193, 'SIBIU': 253, 'TIMISOARA': 329, 'URZICENI': 80, 'VASLUI': 199, 'ZERIND': 374
              }


def mainSearch(app, vem, vai, opcao):
    origem = str(vem).strip().upper()  # Garante que é string
    destino = str(vai).strip().upper()
    metodo = opcao

    if origem not in nos or destino not in nos:
        return "Cidade não está na lista"  # Retorna string se cidades forem inválidas

    path = None
    result = searchPath()

    if metodo == "AMPLITUDE":
        path = result.amplitude(origem, destino, nos, grafo)
    elif metodo == "PROFUNDIDADE":
        path = result.profundidade(origem, destino, nos, grafo)
    elif metodo == "PROFUNDIDADE_LIMITADA":
        path = result.prof_limitada(origem, destino, nos, grafo, 5)
    elif metodo == "APROFUNDAMENTO_ITERATIVO":
        path = result.aprof_iterativo(origem, destino, nos, grafo, len(nos))
    elif metodo == "BIDIRECIONAL":
        path = result.bidirecional(origem, destino, nos, grafo)
    elif metodo == "CUSTO_UNIFORME":
        path = result.custo_uniforme(origem, destino, nos, grafo)
    elif metodo == "GREEDY":
        path = result.greedy(origem, destino, nos, grafo, heuristica)
    elif metodo == "A_ESTRELA":
        path = result.a_estrela(origem, destino, nos, grafo, heuristica)
    elif metodo == "AIA_ESTRELA":
        path = result.aia_estrela(
            origem, destino, nos, grafo, heuristica, len(nos))

    # Si achou u caminho, plota o gráfico
    return path if path else "Caminho não encontrado"
