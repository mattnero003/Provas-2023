import networkx as nx
import tkinter as tk
from tkinter import ttk
def dijkstra(graph, start, end):
    # Calcula os caminhos mínimos a partir do nó de origem
    path = nx.shortest_path(graph, source=start, target=end, weight='weight')
    # Calcula o custo total do caminho
    cost = nx.shortest_path_length(graph, source=start, target=end, weight='weight')

    return path, cost


def main():
    # Criando o grafo com as cidades e suas distâncias
    graph = nx.Graph()
    graph.add_edge('São Paulo', 'Rio de Janeiro', weight=430)
    graph.add_edge('São Paulo', 'Vitória', weight=1100)
    graph.add_edge('Rio de Janeiro', 'Vitória', weight=520)
    graph.add_edge('Vitória', 'Recife', weight=1370)
    graph.add_edge('Recife', 'Salvador', weight=850)
    graph.add_edge('Salvador', 'Natal', weight=820)

    # Solicitar ao usuário a cidade de origem e destino
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")

    # Verificar se as cidades existem no grafo
    if origem not in graph.nodes or destino not in graph.nodes:
        print("Cidade de origem ou destino não encontrada.")
        return

    # Executar o algoritmo de Dijkstra
    caminho, custo = dijkstra(graph, origem, destino)

    # Exibir o resultado
    print(f"Caminho mínimo de {origem} para {destino}: {caminho}")
    print(f"Custo do caminho: {custo} km")


if __name__ == "__main__":
    main()
