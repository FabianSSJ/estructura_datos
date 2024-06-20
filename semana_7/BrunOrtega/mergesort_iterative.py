def mergesort_iterative(arr):
    n = len(arr)
    width = 1
    while width < n:
        left = 0
        while left < n:
            mid = left + width
            right = min(mid + width, n)
            arr[left:right] = merge(arr[left:mid], arr[mid:right])
            left = right
        width *= 2
    return arr

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
    arr = mergesort_iterative(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()