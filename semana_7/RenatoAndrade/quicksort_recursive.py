def recursive(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]
        return quicksort_recursive(left) + [pivot] + quicksort_recursive(right)

if __name__ == "__main__":
    array = [8,10,6,55,100,99,1]
    sorted_arr = quicksort_recursive(array)
    print("Arreglo ordenado:", sorted_arr)
