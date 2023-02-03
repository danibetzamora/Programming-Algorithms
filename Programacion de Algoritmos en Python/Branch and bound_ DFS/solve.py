from node import *

def solve_branch_and_bound_DFS(capacity, items, record_visiting_order=False):
    """"
    :param capacity: capacidad de la mochila
    :param items: items de la mochila
    :param record_visiting_order: activa/desactiva el registro de nodos visitados
    :return: Por ahora sólo devuelve la lista de nodos visitados
    """

    # Completa este código para realizar el recorrido DFS; tienes
    # indicados los sitios que debes completar con tres puntos
    # suspensivos ("...")

    # Utilizamos la lista 'alive' como nuestra pila de nodos vivos
    # (pendientes de visitar) para programar nuestro recorrido DFS.

    alive = []

    # Utilizamos la lista Visiting_Order como el registro de nodos
    # visitados (el contenido final de esta lista lo utiliza el VPL
    # para comprobar que nuestro recorrido DFS es correcto).

    visiting_order = []

    value = 0

    taken = []

    # 1) Creamos el nodo raiz (en este VPL todavía no utilizamos los
    #    parámetros taken, value, room, con lo que se inicializan con
    #    lista vacía y 0). El único valor necesario en el nodo es el
    #    indice al primer elemento de la lista (index = 0).

    root_node = Node(0, [], 0, capacity)

    # Lo añadimos a la lista de nodos vivos (alive)

    alive.append(root_node)

    # Mientras haya nodos en la lista de nodos vivos

    while len(alive) != 0:  # sustituir el True por la condición que considere más adecuada

        # Avanzamos al siguiente nodo de nuestro recorrido DFS (hacemos un pop
        # de la lista) y lo registramos en nuestro recorrido DFS.

        current = alive.pop()
        if record_visiting_order:
            visiting_order.append(current.index)

        if current.room < 0:
            continue

        if current.estimate(items) <= value:
            continue

        if current.value > value:
            value = current.value
            taken = current.taken

        if current.index < len(items):
            alive.append(Node(current.index + 1, current.taken, current.value, current.room))
            current_copy = current.taken.copy()
            current_copy.append(items[current.index].index)
            alive.append(Node(current.index + 1, current_copy, current.value + items[current.index].value, current.room - items[current.index].weight))

    return value, taken, visiting_order
