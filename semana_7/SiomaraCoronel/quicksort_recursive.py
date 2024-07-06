# Definimos la función quicksort_recursivo que toma tres argumentos:
def quicksort_recursivo(array, bajo, alto):
  if bajo < alto:
    # Si el índice bajo es menor que el índice alto, significa que el subarreglo tiene más de un elemento y necesita ser ordenado.
    pivote = particionar(array, bajo, alto)
    quicksort_recursivo(array, bajo, pivote - 1)
    quicksort_recursivo(array, pivote + 1, alto)
  # Devolvemos el array ordenado.
  return array

# Definimos la función particionar que toma tres argumentos:
def particionar(array, bajo, alto):
  # Seleccionamos el último elemento del subarreglo como pivote.
  pivote = array[alto]
  i = bajo - 1

  for j in range(bajo, alto):
    # Si el elemento actual es menor o igual que el pivote:
    if array[j] <= pivote:
      # Incrementamos el índice 'i'.
      i += 1
      # Intercambiamos el elemento en 'i' con el elemento en 'j'.
      array[i], array[j] = array[j], array[i]
  # Colocamos el pivote en su posición correcta intercambiándolo con el elemento en 'i + 1'.
  array[i + 1], array[alto] = array[alto], array[i + 1]
  return i + 1

# Ejemplo de ejecución
# Definimos una lista desordenada.
array = [5, 2, 4, 1, 3]
# Imprimimos la lista original.
print("Arreglo original:", array)
# Imprimimos la lista ordenada.
print("Arreglo ordenado:",quicksort_recursivo(array, 0, len(array) - 1))