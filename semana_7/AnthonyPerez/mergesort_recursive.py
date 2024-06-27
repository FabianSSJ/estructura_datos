def mergesort(array):
    if len(array) <= 1:
        return array
    medio = len(array) // 2
    return merge(mergesort(array[:medio]), mergesort(array[medio:]))

def merge(izq, der):
    result = []
    while izq and der:
        result.append(min(izq[0], der[0]))
        izq = izq[1:] if len(izq) > 1 else []
        der = der[1:] if len(der) > 1 else []
    result += izq + der
    return result
arr = [10, 7, 8, 9, 1, 5,20,40,50,3,25,23,42,12,43,12,43,12]
sorted_arr = mergesort(arr)
print(sorted_arr)  # Salida: [1]