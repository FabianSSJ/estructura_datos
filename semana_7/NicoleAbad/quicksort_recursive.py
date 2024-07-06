def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

if __name__ == "__main__":
    # Ejemplo de uso
    arreglo = [3, 6, 8, 10, 1, 2, 1]
    print("Arreglo original:", arreglo)
    arreglo_ordenado = quicksort(arreglo)
    print("Arreglo ordenado:", arreglo_ordenado)
