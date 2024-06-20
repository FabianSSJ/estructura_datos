def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    def merge(left, right):
        merged = []
        while left and right:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        merged.extend(left or right)
        return merged
    
    mid = len(arr) // 2
    left_sorted = merge_sort_recursive(arr[:mid])
    right_sorted = merge_sort_recursive(arr[mid:])
    
    return merge(left_sorted, right_sorted)

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Array original:", arr)
    sorted_arr = merge_sort_recursive(arr)
    print("Array ordenado:", sorted_arr)
