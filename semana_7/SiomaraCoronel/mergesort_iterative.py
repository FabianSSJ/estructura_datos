# Definimos la función mergesort_iterativo que toma una lista (array) como argumento.
def mergesort_iterativo(array):
    width = 1
    # Obtenemos la longitud del array.
    n = len(array)

    # Mientras el tamaño del subarreglo (width) sea menor que la longitud del array (n):
    while width < n:
        # Iteramos sobre el array en pasos de 2 * width, procesando subarreglos de tamaño width.
        for i in range(0, n, 2 * width):
            # Obtenemos el subarreglo izquierdo de tamaño width.
            izquierda = array[i:i + width]
            # Obtenemos el subarreglo derecho de tamaño width.
            derecha = array[i + width:i + 2 * width]
            # Inicializamos el índice k al inicio del subarreglo actual.
            k = i
            # Inicializamos los índices l y r para los subarreglos izquierdo y derecho, respectivamente.
            l = r = 0

            # Mientras haya elementos en ambos subarreglos:
            while l < len(izquierda) and r < len(derecha):
                # Si el elemento actual en el subarreglo izquierdo es menor que el elemento actual en el subarreglo derecho:
                if izquierda[l] < derecha[r]:
                    # Colocamos el elemento del subarreglo izquierdo en el array original.
                    array[k] = izquierda[l]
                    # Avanzamos al siguiente elemento en el subarreglo izquierdo.
                    l += 1
                else:
                    array[k] = derecha[r]
                    r += 1
                k += 1

            # Mientras haya elementos restantes en el subarreglo izquierdo:
            while l < len(izquierda):
                # Colocamos el elemento del subarreglo izquierdo en el array original.
                array[k] = izquierda[l]
                l += 1
                k += 1

            # Mientras haya elementos restantes en el subarreglo derecho:
            while r < len(derecha):
                array[k] = derecha[r]
                r += 1
                k += 1
        # Duplicamos el tamaño de los subarreglos a fusionar para la siguiente iteración.
        width *= 2
    # Devolvemos el array ordenado.
    return array

# Ejemplo de ejecución
# Definimos una lista desordenada.
array = [5, 6, 2, 8, 4, 7, 1, 3]
# Imprimimos la lista original.
print("Arreglo original:", array)
# Imprimimos la lista ordenada.
print("Arreglo ordenado:", mergesort_iterativo(array))
