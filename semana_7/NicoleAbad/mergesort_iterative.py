def mergesort_iterativo(lista):
    if len(lista) <= 1:
        return lista

    # Crear sublistas iniciales de tamaño 1
    sublistas = [[item] for item in lista]

    # Iterar mientras haya más de una sublista
    while len(sublistas) > 1:
        nuevas_sublistas = []

        # Mezclar sublistas de dos en dos
        for i in range(0, len(sublistas), 2):
            izquierda = sublistas[i]
            derecha = sublistas[i + 1] if i + 1 < len(sublistas) else []
            nuevas_sublistas.append(fusionar(izquierda, derecha))

        sublistas = nuevas_sublistas

    return sublistas[0]

def fusionar(izquierda, derecha):
    lista_fusionada = []
    i = j = 0

    # Mezclar mientras haya elementos en ambas mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_fusionada.append(izquierda[i])
            i += 1
        else:
            lista_fusionada.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    lista_fusionada.extend(izquierda[i:])
    lista_fusionada.extend(derecha[j:])

    return lista_fusionada

if __name__ == "__main__":
    # Ejemplo de uso
    lista_ejemplo = [3, 6, 8, 10, 1, 2, 1]
    print("Lista original:", lista_ejemplo)
    lista_ordenada = mergesort_iterativo(lista_ejemplo)
    print("Lista ordenada:", lista_ordenada)
