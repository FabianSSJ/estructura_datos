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
    if len(arr) <= 1:
        return arr  # Si la longitud de arr es 1 o menos, ya está ordenado
    
    mid = len(arr) // 2  # Calcular el índice medio del array arr
    left = mergesort(arr[:mid])  # Llamar recursivamente mergesort para la mitad izquierda de arr
    right = mergesort(arr[mid:])  # Llamar recursivamente mergesort para la mitad derecha de arr
    
    return merge(left, right)  # Combinar y ordenar las mitades izquierda y derecha usando merge

if __name__ == "__main__":
    arr = [2, 19, 12, 5, 3, 2, 1]
    print("Original array:", arr)
    sorted_arr = mergesort(arr)
    print("Sorted array:", sorted_arr)


