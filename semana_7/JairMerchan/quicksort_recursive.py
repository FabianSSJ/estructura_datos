def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_recursive(left) + middle + quicksort_recursive(right)

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Array original:", arr)
    sorted_arr = quicksort_recursive(arr)
    print("Array ordenado:", sorted_arr)
