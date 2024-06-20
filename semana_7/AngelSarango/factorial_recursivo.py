def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Ejemplo de uso
if __name__ == "__main__":
    arr = [7, 3, 9, 2, 5, 8, 6]
    print("Lista original:", arr)
    print("Lista ordenada:", quicksort(arr))