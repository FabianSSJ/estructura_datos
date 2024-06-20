def partition(arr, low, high):
    pivot = arr[(low + high) // 2]  # Elegimos el elemento medio como pivote
    i = low - 1  # Iniciamos el índice del elemento más pequeño
    j = high + 1  # Iniciamos el índice del elemento más grande

    while True:
        i += 1
        while arr[i] < pivot:  # Encontramos el primer elemento mayor o igual al pivote
            i += 1
        j -= 1
        while arr[j] > pivot:  # Encontramos el primer elemento menor o igual al pivote
            j -= 1
        if i >= j:
            return j  # Si los índices se cruzan, devolvemos el índice de partición
        arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos los elementos en los índices i y j

def quicksort(arr, low, high):
    stack = [(low, high)]  # Iniciamos la pila con el rango completo del array

    while stack:
        start, end = stack.pop()  # Sacamos un rango de la pila
        if start >= end:
            continue  # Si los índices se cruzan, continuamos con el siguiente rango
        pivot_index = partition(arr, start, end)  # Particionamos el array y obtenemos el índice del pivote
        stack.extend([(start, pivot_index), (pivot_index + 1, end)])  # Añadimos los nuevos rangos a la pila

if __name__ == "__main__":
    arr = [6, 3, 12, 20, 2, 3, 1]  # Lista a ordenar
    print("Original array:", arr)
    quicksort(arr, 0, len(arr) - 1)  # Llamada a la función QuickSort con los límites iniciales
    print("Sorted array:", arr)
