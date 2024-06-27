# Ejercicio de Quick Sort Recursivo

# creamos la función principal de Quick Sort
def quickSort(lista):
    # Llamamos a la función auxiliar que implementa quick sort recursivamente
    quickSortRecursivo(lista, 0, len(lista) - 1)
    return lista

# función auxiliar que implementa el algoritmo de quick sort de forma recursiva
def quickSortRecursivo(lista, bajo, alto):
    if bajo < alto:
        # obtenemos el índice del punto de partición
        pi = particion(lista, bajo, alto)

        # ordenamos recursivamente las dos mitades
        quickSortRecursivo(lista, bajo, pi - 1)
        quickSortRecursivo(lista, pi + 1, alto)

# función que realiza la partición de la lista
def particion(lista, bajo, alto):
    # elegimos el último elemento como pivote
    pivote = lista[alto]

    #inicializamos el índice del menor elemento
    i = bajo - 1

    # iteramos sobre la lista para reordenar los elementos en torno al pivote
    for j in range(bajo, alto):
        if lista[j] < pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    # intercambiamos el pivote con el primer elemento mayor que él
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]

    # retornamos el índice del pivote
    return i + 1

# ejemplo de uso del algoritmo quick sort recursivo
print("")
print("------------------------------------")
print("        Quick Sort Recursivo        ")
print("------------------------------------")
print("")
print(quickSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
print("")
