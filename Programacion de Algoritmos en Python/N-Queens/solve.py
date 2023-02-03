from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]
    """

    solutions_list = []

    # Objeto iterador que generará todas las combinaciones posibles en un tablero n x n
    iterator = My_Iterator(num_queens, num_queens)

    # Mientras haya una combinación disponible en el iterador, se evalúa
    for combination in iterator.next():
        # Variable de control, la cual se iguala a 1 cuando una combinación no cumple las condiciones para ser válida
        control = 0

        # Se obtiene una posición de la combinación para ser comparada con el resto
        for i in range(0, len(combination)):
            # Se establece la variable cont, que aumentará en uno cada vez que comprobemos la siguiente columna
            # De esta manera, se comprobará si la dama del primer bucle está en diagonal con otra dama de las siguientes columnas
            cont = 1

            # Segundo bucle que iterará sobre el resto de posiciones de la combinación (i+1)
            for j in range(i+1, len(combination)):
                # Si la posición del primer bucle es igual a otra posición existente en la combinación evaluada, control = 1 y salimos del bucle
                if combination[i] == combination[j]:
                    control = 1
                    break
                # Si la posición del primer bucle es igual al resto de posiciones + cont || - cont (Ambas posiciones están en diagonal), control = 1 y salimos del bucle
                if (combination[i] == combination[j] + cont) | (combination[i] == combination[j] - cont):
                    control = 1
                    break
                # Incrementamos la variable cont para comprobar la diagonal de la posición del primer bucle con el resto de columnas
                cont += 1

            # Si control es igual a 1, dejamos de hacer comprobaciones para esta combinación
            if control == 1:
                break

        # Si control es igual a 1, continuamos con la siguiente combinación del Iterador
        if control == 1:
            continue

        # Si la combinación es válida, se añade a la lista de soluciones
        solutions_list.append(combination)

    return solutions_list