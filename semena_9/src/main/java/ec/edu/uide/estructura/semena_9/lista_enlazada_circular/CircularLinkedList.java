/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.lista_enlazada_circular;

/**
 *
 * @author desarrollo
 */
public class CircularLinkedList {

    private Node last;
    private int size;

    public CircularLinkedList() {
        last = null;
        size = 0;
    }

    /**
     * Método para agregar una nueva canción al final de la lista de
     * reproducción.
     *
     * @param data Nombre de la canción a agregar.
     */
    public void add(String data) {
        Node newNode = new Node(data); // Crea un nuevo nodo con el dato proporcionado
        if (last == null) {
            // Si la lista está vacía
            last = newNode; // El nuevo nodo se convierte en el último nodo
            last.next = last; // El nodo se enlaza consigo mismo, formando el ciclo
        } else {
            // Si la lista no está vacía
            newNode.next = last.next; // El nuevo nodo apunta al primer nodo
            last.next = newNode; // El último nodo actual apunta al nuevo nodo
            last = newNode; // El nuevo nodo se convierte en el último nodo
        }
        size++; // Incrementa el tamaño de la lista
    }

    /**
     * Método para agregar una nueva canción al inicio de la lista de
     * reproducción.
     *
     * @param data Nombre de la canción a agregar.
     */
    public void addFirst(String data) {
        // Crear un nuevo nodo con el dato proporcionado
        Node newNode = new Node(data);

        // Verificar si la lista está vacía
        if (last == null) {
            // Si la lista está vacía, el nuevo nodo se convierte en el último nodo
            last = newNode;
            // El nuevo nodo se enlaza consigo mismo, formando el ciclo
            last.next = last;
        } else {
            // Si la lista no está vacía
            // El nuevo nodo apunta al primer nodo actual
            newNode.next = last.next;
            // El último nodo actual apunta al nuevo nodo
            last.next = newNode;
        }

        // Incrementar el tamaño de la lista
        size++;
    }

    /**
     * Método para eliminar una canción específica de la lista de reproducción.
     *
     * @param data Nombre de la canción a eliminar.
     * @return true si la canción fue eliminada, false en caso contrario.
     */
    public boolean remove(String data) {
        // Verificar si la lista está vacía
        if (last == null) {
            return false; // No se puede eliminar nada de una lista vacía
        }

        // Inicializar dos punteros: 'current' para recorrer la lista y 'previous' para seguir el nodo anterior
        Node current = last.next;
        Node previous = last;

        // Recorrer la lista circular
        do {
            // Verificar si el nodo actual contiene el dato a eliminar
            if (current.data.equals(data)) {
                // * Caso: El nodo a eliminar es el último nodo
                if (current == last) {
                    // Si es el único nodo en la lista
                    if (last.next == last) {
                        last = null; // La lista se convierte en vacía
                    } else {
                        // Si hay más de un nodo
                        previous.next = current.next; // El nodo anterior salta el nodo actual
                        last = previous; // Actualizar 'last' para que sea el nodo anterior
                    }
                } else {
                    // * Caso: El nodo a eliminar no es el último nodo
                    previous.next = current.next; // El nodo anterior salta el nodo actual
                }
                size--; // Decrementar el tamaño de la lista
                return true; // Indicar que el nodo fue eliminado exitosamente
            }
            // Avanzar al siguiente nodo
            previous = current;
            current = current.next;
        } while (current != last.next); // Continuar hasta recorrer toda la lista

        return false; // Si no se encontró el nodo, retornar false
    }

    /**
     * Método para mostrar todas las canciones en la lista de reproducción.
     */
    public void display() {
        if (last == null) {
            System.out.println("La lista está vacía.");
            return;
        }

        Node current = last.next;
        do {
            System.out.print(current.data + " ");
            current = current.next;
        } while (current != last.next);
        System.out.println();
    }

    /**
     * Método para obtener el tamaño de la lista de reproducción.
     *
     * @return Número de canciones en la lista de reproducción.
     */
    public int size() {
        return size;
    }
}
