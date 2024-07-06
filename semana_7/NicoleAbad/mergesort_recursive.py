def mergesort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir la lista en dos mitades
    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    # Llamadas recursivas para ordenar cada mitad
    mitad_izquierda = mergesort(mitad_izquierda)
    mitad_derecha = mergesort(mitad_derecha)

    # Mezclar las dos mitades ordenadas
    return mezclar(mitad_izquierda, mitad_derecha)

def mezclar(izquierda, derecha):
    lista_mezclada = []
    indice_izquierda = indice_derecha = 0

    # Mezclar mientras haya elementos en ambas mitades
    while indice_izquierda < len(izquierda) and indice_derecha < len(derecha):
        if izquierda[indice_izquierda] < derecha[indice_derecha]:
            lista_mezclada.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            lista_mezclada.append(derecha[indice_derecha])
            indice_derecha += 1

    # Agregar los elementos restantes
    lista_mezclada.extend(izquierda[indice_izquierda:])
    lista_mezclada.extend(derecha[indice_derecha:])

    return lista_mezclada

if __name__ == "__main__":
    # Ejemplo de uso
    ejemplo_lista = [3, 6, 8, 10, 1, 2, 1]
    print("Lista original:", ejemplo_lista)
    lista_ordenada = mergesort(ejemplo_lista)
    print("Lista ordenada:", lista_ordenada)
S