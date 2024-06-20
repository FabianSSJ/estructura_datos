def iterative(array):
    width = 1
    n = len(array)
    while width < n:
        for i in range(0, n, 2 * width):
            left = array[i:i + width]
            right = array[i + width:i + 2 * width]
            array[i:i + 2 * width] = merge(left, right)
        width *= 2
    return array

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

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    array = [8,10,6,55,100,99,1]
    sorted_array = mergesort_iterative(array)
    print("Arrayeglo ordenado:", sorted_array)
