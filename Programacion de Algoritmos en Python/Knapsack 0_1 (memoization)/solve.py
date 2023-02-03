# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_memoization(items, capacity):
    mem={}

    # Utilizaremos esta función para generar la clave de acceso al
    # diccionario que utilizamos para guardar los resultados (mem).

    # Recordatorio de la documentación de Python 3:
    #    "Keys can be any immutable type; strings and numbers can
    #     always be keys. Tuples can be used as keys if they contain
    #     only strings, numbers, or tuples"
    
    def getKey(n, w):
        return (n, w)    # Retornamos la clave

    def t(n, w):
        key = getKey(n, w)

        if key not in mem:
            if n < 0:
                value = 0

            elif w <= 0:
                value = 0

            elif items[n].weight > w:
                value = t(n-1, w)

            else:
                value = max(t(n-1, w), t(n-1, w-items[n].weight) + items[n].value)

            mem[key] = value

        return mem[key]

    n = len(items) - 1
    max_value = t(n, capacity)

    return max_value
