import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """
    distance = {}  # Diccionario con la distancia desde
                   # firstNode al resto de los nodos.

    for node in graph.nodes():
        distance[node] = infinite

    visited = []
    queue = Queue()

    visited.append(first_node)
    queue.enqueue(first_node)
    distance[first_node] = 0

    while not queue.isEmpty():
        node = queue.dequeue()

        for edge in graph.neighbors(node):
            if edge not in visited:
                visited.append(edge)
                distance[edge] = distance[node] + 1
                queue.enqueue(edge)

    return distance
