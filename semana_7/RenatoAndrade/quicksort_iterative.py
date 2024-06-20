def iterative(array):
    stack = [(0, len(array) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = array[end]
        low = start

        for i in range(start, end):
            if array[i] < pivot:
                array[i], array[low] = array[low], array[i]
                low += 1

        array[low], array[end] = array[end], array[low]

        stack.append((start, low - 1))
        stack.append((low + 1, end))

    return array

if __name__ == "__main__":
    array = [8,10,6,55,100,99,1]
    sorted_array = quicksort_iterative(array)
    print("Arrayeglo ordenado:", sorted_array)
