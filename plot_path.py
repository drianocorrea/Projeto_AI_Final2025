import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH


def load_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    nodes = lines[0].strip().split(',')
    edges = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        if len(parts) > 1:
            source = parts[0]
            for target in parts[1:]:
                edges.append((source, target))
    return nodes, edges


def plot_graph(nodes, edges, path=None, frame=None):
    # Limpa o frame anterior
    for widget in frame.winfo_children():
        widget.destroy()

    # Cria a figura do matplotlib
    fig = plt.figure(figsize=(7, 6))
    G = nx.Graph()

    # Adiciona nós e arestas
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Define o layout
    pos = nx.spring_layout(G, seed=42)

    # Desenha o grafo base
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=5)

    # Destaca o caminho se existir
    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               width=2, edge_color='red')
        nx.draw_networkx_nodes(G, pos, nodelist=path,
                               node_size=200, node_color='red')

    plt.title("Caminho entre Cidades")
    plt.axis('off')

    # Converte a figura para widget Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)


"""def plot_graph(nodes, edges, path=None):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)  # Layout consistente

    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

    if path:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               width=2, edge_color='red')
        nx.draw_networkx_nodes(G, pos, nodelist=path,
                               node_size=700, node_color='red')

    plt.title("Grafo de Cidades e Caminho Encontrado")
    plt.axis('off')
    plt.show()"""
