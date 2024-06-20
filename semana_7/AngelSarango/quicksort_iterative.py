def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[start]
        low = start + 1
        high = end

        while low <= high:
            while low <= high and arr[low] <= pivot:
                low += 1
            while low <= high and arr[high] > pivot:
                high -= 1
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]

        arr[start], arr[high] = arr[high], arr[start]

        stack.append((start, high - 1))
        stack.append((high + 1, end))

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    arr = [12, 4, 7, 3, 10, 6, 1]
    print("Lista original:", arr)
    print("Lista ordenada:", quicksort_iterative(arr))