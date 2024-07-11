/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.lista_enlazada_doble_circular;

/**
 *
 * @author desarrollo
 */
public class DoublyCircularLinkedList {

    private Node head;
    private Node tail;
    private int size;

    public DoublyCircularLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

    /**
     * Método para agregar un nodo al final de la lista.
     *
     * @param data El valor del nodo a agregar.
     */
    public void add(int data) {
        Node newNode = new Node(data); // Crear un nuevo nodo con el dato proporcionado
        if (head == null) { // Si la lista está vacía
            head = newNode; // El nuevo nodo se convierte en el primer nodo (head)
            tail = newNode; // El nuevo nodo también se convierte en el último nodo (tail)
            head.next = head; // El siguiente nodo de head apunta a sí mismo
            head.prev = head; // El nodo previo de head apunta a sí mismo
        } else {
            tail.next = newNode; // El siguiente nodo de tail apunta al nuevo nodo
            newNode.prev = tail; // El nodo previo del nuevo nodo apunta a tail
            newNode.next = head; // El siguiente nodo del nuevo nodo apunta a head
            head.prev = newNode; // El nodo previo de head apunta al nuevo nodo
            tail = newNode; // El nuevo nodo se convierte en el último nodo (tail)
        }
        size++; // Incrementar el tamaño de la lista
    }

    /**
     * Método para agregar un nodo al inicio de la lista.
     *
     * @param data El valor del nodo a agregar.
     */
    public void addFirst(int data) {
        Node newNode = new Node(data); // Crear un nuevo nodo con el dato proporcionado
        if (head == null) { // Si la lista está vacía
            head = newNode; // El nuevo nodo se convierte en el primer nodo (head)
            tail = newNode; // El nuevo nodo también se convierte en el último nodo (tail)
            head.next = head; // El siguiente nodo de head apunta a sí mismo
            head.prev = head; // El nodo previo de head apunta a sí mismo
        } else {
            newNode.next = head; // El siguiente nodo del nuevo nodo apunta a head
            newNode.prev = tail; // El nodo previo del nuevo nodo apunta a tail
            head.prev = newNode; // El nodo previo de head apunta al nuevo nodo
            tail.next = newNode; // El siguiente nodo de tail apunta al nuevo nodo
            head = newNode; // El nuevo nodo se convierte en el primer nodo (head)
        }
        size++; // Incrementar el tamaño de la lista
    }

    -/**
     * Método para eliminar un nodo con un valor específico de la lista.
     *
     * @param data El valor del nodo a eliminar.
     * @return true si el nodo fue eliminado, false si no se encontró el nodo.
     */
    public boolean remove(int data) {
        if (head == null) {
            return false; // Si la lista está vacía, retornar false
        }
        Node current = head; // Empezar desde el primer nodo
        do {
            if (current.data == data) { // Si se encuentra el nodo con el dato proporcionado
                if (current == head && current == tail) { // Si es el único nodo en la lista
                    head = null; // La lista se convierte en vacía
                    tail = null;
                } else {
                    if (current == head) { // Si el nodo a eliminar es el primero (head)
                        head = head.next; // Mover head al siguiente nodo
                        head.prev = tail; // El nodo previo de head apunta a tail
                        tail.next = head; // El siguiente nodo de tail apunta a head
                    } else if (current == tail) { // Si el nodo a eliminar es el último (tail)
                        tail = tail.prev; // Mover tail al nodo previo
                        tail.next = head; // El siguiente nodo de tail apunta a head
                        head.prev = tail; // El nodo previo de head apunta a tail
                    } else { // Si el nodo a eliminar está en el medio
                        current.prev.next = current.next; // El siguiente nodo del nodo previo apunta al siguiente nodo del nodo actual
                        current.next.prev = current.prev; // El nodo previo del siguiente nodo apunta al nodo previo del nodo actual
                    }
                }
                size--; // Decrementar el tamaño de la lista
                return true; // Retornar true si el nodo fue eliminado
            }
            current = current.next; // Mover al siguiente nodo
        } while (current != head); // Continuar hasta recorrer toda la lista

        return false; // Retornar false si el nodo no se encontró
    }

    /**
     * Método para mostrar los elementos de la lista en orden.
     */
    public void display() {
        if (head == null) {
            System.out.println("The list is empty."); // Imprimir mensaje si la lista está vacía
            return;
        }

        Node current = head; // Empezar desde el primer nodo
        do {
            System.out.print(current.data + " "); // Imprimir el dato del nodo actual
            current = current.next; // Mover al siguiente nodo
        } while (current != head); // Continuar hasta regresar al primer nodo
        System.out.println(); // Nueva línea al final de la lista
    }

    /**
     * Método para mostrar los elementos de la lista en orden inverso.
     */
    public void displayReverse() {
        if (tail == null) {
            System.out.println("The list is empty."); // Imprimir mensaje si la lista está vacía
            return;
        }

        Node current = tail; // Empezar desde el último nodo
        do {
            System.out.print(current.data + " "); // Imprimir el dato del nodo actual
            current = current.prev; // Mover al nodo previo
        } while (current != tail); // Continuar hasta regresar al último nodo
        System.out.println(); // Nueva línea al final de la lista
    }

    /**
     * Método para obtener el tamaño de la lista.
     *
     * @return Número de nodos en la lista.
     */
    public int size() {
        return size;
    }

}
