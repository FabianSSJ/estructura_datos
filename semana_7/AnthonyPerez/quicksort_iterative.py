def quicksort_iterativo(array):
    if len(array) <= 1:
        return array
    pila = [(0, len(array) - 1)]
    while len(pila) > 0:
        a, b = pila.pop()
        pivote = array[b]
        i = a
        for j in range(a, b):
            if array[j] < pivote:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[b] = array[b], array[i]
        pila.extend((a, i - 1) if i > a + 1 else [] for i in range(i + 1, b + 1))
    return array
arr = [10, 7, 8, 9, 1, 5,20,40,50,3,25,23,42,12,43,12,43,12]
sorted_arr = quicksort_iterativo(arr)
print(sorted_arr)  # Salida: [1, 5, 7, 8, 9, 10]