def recursive(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergesort_recursive(array[:mid])
    right = mergesort_recursive(array[mid:])

    return merge(left, right)

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
    sorted_array = mergesort_recursive(array)
    print("arrayeglo ordenado:", sorted_array)
