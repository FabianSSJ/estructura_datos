def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))

    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    arr[low], arr[j] = arr[j], arr[low]
    return j

# Example usage
arr = [5, 2, 8, 3, 1, 6, 4]
arr = quicksort_iterative(arr)
print("Sorted array:", arr)