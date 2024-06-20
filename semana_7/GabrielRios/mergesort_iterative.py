def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, width * 2):
            left = arr[i:i+width]
            right = arr[i+width:i+width*2]
            arr[i:i+width*2] = merge(left, right)
        width *= 2
    return arr

if __name__ == "__main__":
    arr = [1, 8, 12, 5, 7, 9, 7]
    print("Original array:", arr)
    sorted_arr = mergesort(arr)
    print("Sorted array:", sorted_arr)
