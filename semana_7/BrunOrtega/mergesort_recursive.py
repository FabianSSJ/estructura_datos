def mergesort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort_recursive(arr[:mid])
    right = mergesort_recursive(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def main():
    arr = [5, 2, 8, 3, 1, 6, 4]
    arr = mergesort_recursive(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()