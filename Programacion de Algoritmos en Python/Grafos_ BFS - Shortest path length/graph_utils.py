import networkx as nx

def build_graph():
    # Añade aqui el código que hiciste en el ejercicio de la 
    # semana anterior para crear un grafo no-dirigido.

    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    # Paso 1: Crear un grafo unidirecional con num_nodes
    graph = nx.Graph()
    graph.add_nodes_from([n for n in range(1, num_nodes + 1)])

    # Paso 2: Añadirle las aristas
    for x in range(num_edges):
        input_edge = input().split()
        graph.add_edge(int(input_edge[0]), int(input_edge[1]))

    return graph
    