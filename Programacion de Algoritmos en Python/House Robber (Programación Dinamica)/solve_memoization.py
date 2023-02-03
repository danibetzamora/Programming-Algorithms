# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}

    # Utiliza esta función para programar el código de
    # tu recurrencia utilizando memoization.
    #   Aviso: Para resolver este ejercicio no es valido
    #          utilizar el soporte de @functools
    def t(n):
        key = n

        if key not in mem:
            if n < 0:
                result = 0
            else:
                result = max(t(n-2) + items[n], t(n-1))

            mem[key] = result

        return mem[key]

    return t(len(items)-1)
