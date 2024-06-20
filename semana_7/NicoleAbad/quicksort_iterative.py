def quicksort_iterativo(lista):
    def particionar(lista, inicio, fin):
        pivote = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j] <= pivote:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
        return i + 1

    stack = [(0, len(lista) - 1)]

    while stack:
        inicio, fin = stack.pop()
        if inicio < fin:
            p = particionar(lista, inicio, fin)
            stack.append((inicio, p - 1))
            stack.append((p + 1, fin))

    return lista

if __name__ == "__main__":
    # Ejemplo de uso
    arreglo = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", arreglo)
    arreglo_ordenado = quicksort_iterativo(arreglo)
    print("Ordenado:", arreglo_ordenado)
