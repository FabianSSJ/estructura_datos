def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr.pop()
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)
arr = [10, 7, 8, 9, 1, 5,20,40,50,3,25,23,42,12,43,12,43,12]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Salida: [1, 5, 7, 8, 9, 10]