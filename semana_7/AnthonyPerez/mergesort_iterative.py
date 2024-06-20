def mergesort_iterativo(array):
    if len(array) <= 1:
        return array
    resultado = [array[:] for _ in range(len(array))]
    tamaño = 1
    while tamaño < len(array):
        for inicio in range(0, len(array), 2 * tamaño):
            resultado[inicio:inicio + 2 * tamaño] = merge(resultado[inicio:inicio + tamaño], resultado[inicio + tamaño:inicio + 2 * tamaño] if inicio + 2 * tamaño < len(array) else [])
        tamaño *= 2
    return resultado[0]

def merge(izq, der):
    result = []
    while izq and der:
        result.append(min(izq[0], der[0]))
        izq = izq[1:] if len(izq) > 1 else []
        der = der[1:] if len(der) > 1 else []
    result += izq + der
    return result
arr = [10, 7, 8, 9, 1, 5,20,40,50,3,25,23,42,12,43,12,43,12]
sorted_arr = mergesort_iterativo(arr)
print(sorted_arr)  # Salida: [1]