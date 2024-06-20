def merge_sort_iterative(arr):
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
    
    stack = [[x] for x in arr]
    
    while len(stack) > 1:
        stack.append(merge(stack.pop(0), stack.pop(0)))
    
    return stack.pop()

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Array original:", arr)
    sorted_arr = merge_sort_iterative(arr)
    print("Array ordenado:", sorted_arr)
