def mergesort_recursive(arr):
    """
    Ordena una lista utilizando el algoritmo de MergeSort de manera recursiva.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada.

    Ejemplo de uso:
    >>> mergesort_recursive([38, 27, 43, 3, 9, 82, 10])
    [3, 9, 10, 27, 38, 43, 82]
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = mergesort_recursive(arr[:middle])
    right = mergesort_recursive(arr[middle:])

    return merge(left, right)

def merge(left, right):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.

    Parámetros:
    left (list): La primera lista ordenada.
    right (list): La segunda lista ordenada.

    Retorna:
    list: La lista combinada y ordenada.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", arr)
    sorted_arr = mergesort_recursive(arr)
    print("Ordenado:", sorted_arr)
