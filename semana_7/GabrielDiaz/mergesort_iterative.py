# Ejercicio de Merge Sort Iterativo

# Creamos la función principal de Merge Sort
def mergeSort(lista):
    # Inicializamos el tamaño actual de sublistas
    tamaño_actual = 1
    n = len(lista)

    # Iteramos sobre los tamaños de sublistas
    while tamaño_actual < n:
        # Iteramos sobre los índices de las sublistas
        for inicio in range(0, n, 2 * tamaño_actual):
            # Calculamos los puntos medios y finales de las sublistas
            medio = min(inicio + tamaño_actual - 1, n - 1)
            fin = min(inicio + 2 * tamaño_actual - 1, n - 1)

            # Realizamos la combinación de las sublistas
            merge(lista, inicio, medio, fin)

        # Doblamos el tamaño de sublistas
        tamaño_actual = 2 * tamaño_actual

    return lista

# Función que realiza la combinación de sublistas
def merge(lista, inicio, medio, fin):
    # Crear sublistas temporales
    izquierda = lista[inicio:medio + 1]
    derecha = lista[medio + 1:fin + 1]

    # Inicializamos los índices de las sublistas y de la lista principal
    i = 0
    j = 0
    k = inicio

    # Combinamos las sublistas ordenadas en la lista principal
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i += 1
        else:
            lista[k] = derecha[j]
            j += 1
        k += 1

    # Copiamos los elementos restantes de la sublista izquierda
    while i < len(izquierda):
        lista[k] = izquierda[i]
        i += 1
        k += 1

    # Copiamos los elementos restantes de la sublista derecha
    while j < len(derecha):
        lista[k] = derecha[j]
        j += 1
        k += 1

# Ejemplo de uso del algoritmo merge sort iterativo
print("")
print("------------------------------------")
print("        Merge Sort Iterativo        ")
print("------------------------------------")
print("")
print(mergeSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
print("")
