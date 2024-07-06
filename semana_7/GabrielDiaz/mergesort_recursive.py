# Ejercicio de Merge Sort Recursivo

# Creamos la función principal de Merge Sort
def mergeSort(lista):
    if len(lista) > 1:
        # Encontramos el punto medio de la lista
        medio = len(lista) // 2

        # Dividimos la lista en dos mitades
        mitad_izquierda = lista[:medio]
        mitad_derecha = lista[medio:]

        # Llamamos recursivamente a mergeSort en cada mitad
        mergeSort(mitad_izquierda)
        mergeSort(mitad_derecha)

        # Inicializamos los índices para iterar sobre las dos mitades y la lista principal
        i = 0
        j = 0
        k = 0

        # Combinamos las dos mitades ordenadas en una sola lista
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Verificamos si quedan elementos en la mitad izquierda
        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        # Verificamos si quedan elementos en la mitad derecha
        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

    # Retornamos la lista ordenada
    return lista

# Ejemplo de uso del algoritmo merge sort recursivo
print("")
print("------------------------------------")
print("        Merge Sort Recursivo        ")
print("------------------------------------")
print("")
print(mergeSort([3, 4, 9, 2, 1, 8, 5, 7, 6]))
print("")
