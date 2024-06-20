def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def mergesort_iterative(arr):
    if len(arr) <= 1:
        return arr

    width = 1
    n = len(arr)

    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            arr[i:i + 2 * width] = merge(left, right)
        width *= 2

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    arr = [13, 8, 15, 2, 7, 1, 5]
    print("Lista original:", arr)
    print("Lista ordenada:", mergesort_iterative(arr))