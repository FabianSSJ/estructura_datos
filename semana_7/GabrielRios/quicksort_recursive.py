def partition(arr, low, high):
    pivot = arr[(low + high) // 2]  # Elegimos el elemento medio como pivote
    i = low - 1  # Inicializamos el índice del elemento más pequeño
    j = high + 1  # Inicializamos el índice del elemento más grande

    while True:
        i += 1
        while arr[i] < pivot:  # Encontramos el primer elemento mayor o igual al pivote
            i += 1
        j -= 1
        while arr[j] > pivot:  # Encontramos el primer elemento menor o igual al pivote
            j -= 1
        if i >= j:
            return j  
        arr[i], arr[j] = arr[j], arr[i]  # Intercambiamos los elementos en los índices i y j

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  # Particionamos el array y obtenemos el índice del pivote
        quicksort(arr, low, pivot_index)  # Aplicamos QuickSort a la sublista izquierda
        quicksort(arr, pivot_index + 1, high)  # Aplicamos QuickSort a la sublista derecha

if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]  # Lista para ordenar 
    print("Original array:", arr)
    quicksort(arr, 0, len(arr) - 1)  # Llamamos a la función QuickSort con los límites iniciales
    print("Sorted array:", arr)
    

