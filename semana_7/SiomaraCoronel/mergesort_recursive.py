# Definimos la función mergesort_recursivo que toma una lista (array) como argumento.
def mergesort_recursivo(array):
    # Si la longitud del array es mayor que 1, significa que el array necesita ser ordenado.
    if len(array) > 1:
        # Calculamos el índice medio del array.
        medio = len(array) // 2
        # Dividimos el array en dos subarreglos: la mitad izquierda.
        izquierda = array[:medio]
        # Dividimos el array en dos subarreglos: la mitad derecha.
        derecha = array[medio:]

        # Llamamos recursivamente a mergesort_recursivo para ordenar el subarreglo izquierdo.
        mergesort_recursivo(izquierda)
        # Llamamos recursivamente a mergesort_recursivo para ordenar el subarreglo derecho.
        mergesort_recursivo(derecha)
        i = j = k = 0

        # Mientras haya elementos en ambos subarreglos:
        while i < len(izquierda) and j < len(derecha):
            # Si el elemento actual en el subarreglo izquierdo es menor que el elemento actual en el subarreglo derecho:
            if izquierda[i] < derecha[j]:
                # Colocamos el elemento del subarreglo izquierdo en el array original.
                array[k] = izquierda[i]
                # Avanzamos al siguiente elemento en el subarreglo izquierdo.
                i += 1
            else:
                array[k] = derecha[j]
                j += 1
            k += 1

        # Mientras haya elementos restantes en el subarreglo izquierdo:
        while i < len(izquierda):
            array[k] = izquierda[i]
            i += 1
            k += 1

        # Mientras haya elementos restantes en el subarreglo derecho:
        while j < len(derecha):
            array[k] = derecha[j]
            j += 1
            k += 1
    # Devolvemos el array ordenado.
    return array

# Ejemplo de ejecución
# Definimos una lista desordenada.
array = [5, 6, 2, 4, 7, 1, 3]
# Imprimimos la lista original.
print("Arreglo original:", array)
# Imprimimos la lista ordenada.
print("Arreglo ordenado:", mergesort_recursivo(array))
