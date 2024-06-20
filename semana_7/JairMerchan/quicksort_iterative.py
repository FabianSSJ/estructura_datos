def quicksort_iterative(arr):
    size = len(arr)
    stack = [(0, size - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[end]
        low = start

        for i in range(start, end):
            if arr[i] < pivot:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1

        arr[low], arr[end] = arr[end], arr[low]

        stack.append((start, low - 1))
        stack.append((low + 1, end))

    return arr

arr = [3, 6, 8, 10, 1, 2, 1]
print("Array original:", arr)
sorted_arr = quicksort_iterative(arr.copy())
print("Array ordenado:", sorted_arr)
