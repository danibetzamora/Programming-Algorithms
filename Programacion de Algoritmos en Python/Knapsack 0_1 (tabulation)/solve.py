# Recurrencia
# -----------
#  t(n,w) = 0                                    : if n <= 0 or w = 0
#         = t(n-1,w)                             : if w(n) > w
#         = max (t(n-1,w), t(n-1,w-w(n)) + B(n))

import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1, capacity+1), dtype=int)

    def fill_table():
        for i in range(1, n + 1):
            for W in range(1, w + 1):
                if items[i - 1].weight <= W:
                    table[i][W] = max(table[i - 1][W], table[i - 1][W - items[i - 1].weight] + items[i - 1].value)
                else:
                    table[i][W] = table[i - 1][W]
        return

    def fill_taken(n, w):
        i = n
        k = w

        while i > 0 and k > 0:
            if table[i][k] != table[i-1][k]:
                taken.insert(0, i)
                i -= 1
                k -= items[i].weight
            else:
                i -= 1

        return

    n = len(items)
    w = capacity
    
    fill_table()                # Relleno la tabla
    fill_taken(n, w)             # Genero la lista de items elegidos

    return table[-1][-1], taken
