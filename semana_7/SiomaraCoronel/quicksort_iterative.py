# Definimos la función quicksort_iterativo que toma una lista (array) como argumento.
def quicksort_iterativo(array):
    # Se crea una pila para almacenar los índices de los subarreglos
    stack = [(0, len(array) - 1)]

    # Mientras la pila no esté vacía, seguimos procesando los subarreglos.
    while stack:
        # Obtenemos los índices del subarreglo actual extrayendo la última tupla de la pila.
        bajo, alto = stack.pop()
        if bajo < alto:
            # Particionamos el subarreglo y obtenemos el índice del pivote
            pivote = particionar(array, bajo, alto)
            # Agregamos los índices de los subarreglos a la pila
            stack.append((bajo, pivote - 1))
            stack.append((pivote + 1, alto))
      # Devolvemos el array ordenado.
    return array

# Definimos la función particionar que toma una lista (array) y dos índices (bajo y alto).
def particionar(array, bajo, alto):
    # Seleccionamos el último elemento del subarreglo como pivote.
    pivote = array[alto]
    # Inicializamos el índice 'i' para los elementos menores que el pivote.
    i = bajo - 1
    for j in range(bajo, alto):
        # Si el elemento actual es menor o igual que el pivote:
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[alto] = array[alto], array[i + 1]
    # Devolvemos la posición del pivote.
    return i + 1

# Ejemplo de ejecución
# Definimos una lista desordenada.
array = [5, 6, 2, 4, 1, 3]
# Imprimimos la lista original.
print("Arreglo original:", array)
# Imprimimos la lista ordenada.
print("Arreglo ordenado:", quicksort_iterativo(array))
