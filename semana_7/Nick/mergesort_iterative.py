def quicksort_iterative(arr):
    """
    Ordena una lista utilizando el algoritmo de QuickSort de manera iterativa.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Ejemplo de uso:
    >>> quicksort_iterative([9, 7, 5, 11, 12, 2, 14, 3, 10, 6])
    [2, 3, 5, 6, 7, 9, 10, 11, 12, 14]
    """
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[end]
        left = start
        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[end] = arr[end], arr[left]

        stack.append((start, left - 1))
        stack.append((left + 1, end))

# Ejemplo de uso
if __name__ == "__main__":
    arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
    print("Original:", arr)
    quicksort_iterative(arr)
    print("Ordenado:", arr)

