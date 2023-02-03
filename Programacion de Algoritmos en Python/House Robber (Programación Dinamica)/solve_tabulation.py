# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    
    def fill_table():
        if len(items) == 0:
            return 0

        table.append(items[0])

        if len(items) > 1:
            table.append(max(table[0], items[1]))

        for i in range(2, len(items)):
            table.append(max(table[i-2] + items[i], table[i-1]))

        return

    fill_table()

    max_benefit = table[-1]     # El máximo beneficio está en el
                                # último elemento de la tabla
    return max_benefit
