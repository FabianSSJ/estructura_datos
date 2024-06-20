def mergesort_iterative(arr):
    """
    Ordena una lista utilizando el algoritmo de MergeSort de manera iterativa.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Ejemplo de uso:
    >>> mergesort_iterative([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2

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
    arr = [5, 4, 3, 2, 1]
    print("Original:", arr)
    mergesort_iterative(arr)
    print("Ordenado:", arr)
