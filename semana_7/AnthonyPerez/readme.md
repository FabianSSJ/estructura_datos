# Algoritmos de Ordenamiento en Python
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://th.bing.com/th/id/OIP.EDJ9xoErBbZqK2tExVoJfAAAAA?rs=1&pid=ImgDetMain" alt="Python Logo" width="100">
    </a>
    <a href="https://flet.io/">
        <img src="https://avatars.githubusercontent.com/u/102273996?v=4" alt="Flet Logo" width="100">
    </a>  
</p>

Este repositorio contiene implementaciones de los algoritmos de ordenamiento QuickSort y MergeSort en Python, tanto de forma recursiva como iterativa. A continuación, se detallan los archivos incluidos y su descripción:

## Archivos

1. `quicksort_recursivo.py`: Implementación recursiva del algoritmo QuickSort.
2. `quicksort_iterativo.py`: Implementación iterativa del algoritmo QuickSort.
3. `mergesort_recursivo.py`: Implementación recursiva del algoritmo MergeSort.
4. `mergesort_iterativo.py`: Implementación iterativa del algoritmo MergeSort.

## Descripción

### QuickSort

QuickSort es un algoritmo de ordenamiento eficiente que se basa en el principio de "divide y vencerás". Sigue los siguientes pasos:

1. Selecciona un elemento de la lista como pivote.
2. Divide la lista en dos sublistas: una con los elementos menores que el pivote y otra con los elementos mayores o iguales que el pivote.
3. Ordena recursivamente cada una de las sublistas.
4. Combina las sublistas ordenadas con el pivote en el medio.

La complejidad temporal promedio de QuickSort es O(n log n), pero en el peor de los casos (cuando la lista está ordenada o inversamente ordenada), su complejidad es O(n^2).

### MergeSort

MergeSort es otro algoritmo de ordenamiento eficiente que también sigue el principio de "divide y vencerás". Funciona de la siguiente manera:

1. Divide la lista de entrada en dos mitades hasta que cada sublista contenga un solo elemento (caso base).
2. Ordena y combina ("merge") las sublistas individuales en una lista ordenada.
3. Repite el proceso de combinación hasta que se obtenga una sola lista ordenada.

La complejidad temporal de MergeSort es O(n log n) en el peor de los casos.

## Uso

Cada archivo contiene un ejemplo de uso al final del código. Simplemente ejecuta el archivo correspondiente para ver el resultado del algoritmo de ordenamiento aplicado a una lista de ejemplo.

```python
# Ejemplo de uso
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)  # o merge_sort(arr)
print(sorted_arr)  # Salida: [1, 5, 7, 8, 9, 10]
```

Puedes modificar la lista de ejemplo `arr` según tus necesidades para probar los algoritmos con diferentes entradas.

## Consideraciones adicionales:

La elección del algoritmo de ordenamiento depende de factores como el tamaño de la lista, la distribución de datos y las restricciones de tiempo y memoria.
Es importante analizar la complejidad computacional de cada algoritmo para comprender su rendimiento en diferentes escenarios.
Existen otras técnicas de ordenamiento como Counting Sort y Radix Sort que pueden ser más eficientes en casos específicos.
Recursos adicionales:

https://en.wikipedia.org/wiki/Sorting_algorithm
https://www.geeksforgeeks.org/videos/merge-sort-hv3scl/
https://www.geeksforgeeks.org/problems/insertion-sort/1
https://www.geeksforgeeks.org/videos/bubble-sort-6gnt0b/
https://www.geeksforgeeks.org/quick-sort/


## Contribuciones

Si deseas contribuir a este repositorio, puedes seguir los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b nueva-rama`).
3. Realiza tus cambios y compromételos (`git commit -am 'Agrega nueva característica'`).
4. Envía tus cambios (`git push origin nueva-rama`).
5. Abre un Pull Request.

## Nota:

Este README es un resumen básico de los ejercicios realizados. Se recomienda revisar el código y las explicaciones detalladas proporcionadas en las sesiones anteriores para una comprensión completa.