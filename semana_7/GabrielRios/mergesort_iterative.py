def merge(left, right):
    result = []  # Lista donde se almacenará el resultado combinado y ordenado
    i, j = 0, 0   # Índices para recorrer las listas left y right respectivamente
    
    # Iterar mientras haya elementos tanto en left como en right por recorrer
    while i < len(left) and j < len(right):
        # Comparar los elementos actuales de left y right
        if left[i] < right[j]:
            result.append(left[i])  # Agregar el elemento de left a result
            i += 1  # Mover el índice i al siguiente elemento de left
        else:
            result.append(right[j])  # Agregar el elemento de right a result
            j += 1  # Mover el índice j al siguiente elemento de right
    
    # Agregar los elementos restantes de left y right (si los hay) a result
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result  # Devolver la lista combinada y ordenada

def mergesort(arr):
    width = 1  # Ancho inicial de los subarrays a combinar
    n = len(arr)  # Longitud del array arr
    while width < n:
        for i in range(0, n, width * 2):
            left = arr[i:i+width]  # Subarray izquierdo
            right = arr[i+width:i+width*2]  # Subarray derecho
            arr[i:i+width*2] = merge(left, right)  # Combinar y ordenar los subarrays
        width *= 2  # Duplicar el ancho para el próximo nivel de combinación
    return arr

if __name__ == "__main__":
    arr = [1, 8, 12, 5, 7, 9, 7]
    print("Original array:", arr)
    sorted_arr = mergesort(arr)
    print("Sorted array:", sorted_arr)
