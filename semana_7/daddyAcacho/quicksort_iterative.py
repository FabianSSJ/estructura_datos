def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        
        pivot_index = partition(arr, start, end)
        stack.append((start, pivot_index - 1))
        stack.append((pivot_index + 1, end))
        
    return arr

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    print("Sorted array:", quicksort(arr))
