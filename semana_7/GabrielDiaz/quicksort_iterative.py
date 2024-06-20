# Ejercicio de Quick Sort Iterativo

# Creamos la función principal de Quick Sort
def quickSort(lista):
    # Llamamos a la función auxiliar que implementa Quick Sort de forma iterativa
    quickSortIterativo(lista, 0, len(lista) - 1)
    return lista

# Función auxiliar que implementa el algoritmo de Quick Sort de forma iterativa
def quickSortIterativo(lista, bajo, alto):
    # Creamos una pila para almacenar los índices
    tamaño = alto - bajo + 1
    pila = [0] * tamaño

    # Inicializamos la pila con los índices iniciales
    tope = 0
    pila[tope] = bajo
    tope = tope + 1
    pila[tope] = alto

    # Iteramos mientras la pila no esté vacía
    while tope >= 0:
        # Sacamos los índices de la pila
        alto = pila[tope]
        tope = tope - 1
        bajo = pila[tope]
        tope = tope - 1

        # Obtenemos el índice del punto de partición
        pi = particion(lista, bajo, alto)

        # Si hay elementos en el lado izquierdo del pivote, los agregamos a la pila
        if pi - 1 > bajo:
            tope = tope + 1
            pila[tope] = bajo
            tope = tope + 1
            pila[tope] = pi - 1

        # Si hay elementos en el lado derecho del pivote, los agregamos a la pila
        if pi + 1 < alto:
            tope = tope + 1
            pila[tope] = pi + 1
            tope = tope + 1
            pila[tope] = alto

# Función que realiza la partición de la lista
def particion(lista, bajo, alto):
    # Elegimos el último elemento como pivote
    pivote = lista[alto]

    # Inicializamos el índice del menor elemento
    i = bajo - 1

    # Iteramos sobre la lista para reordenar los elementos en torno al pivote
    for j in range(bajo, alto):
        if lista[j] < pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    # Intercambiamos el pivote con el primer elemento mayor que él
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]

    # Retornamos el índice del pivote
    return i + 1

# Ejemplo de uso del algoritmo quick sort iterativo
print("")
print("------------------------------------")
print("        Quick Sort Iterativo        ")
print("------------------------------------")
print("")
print(quickSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
print("")
