/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9;

/**
 *
 * @author desarrollo
 * 
 * 
 * 
 * 
 * Variables de la Clase CircularQueue
    size: Un entero que representa la capacidad máxima de la cola. Es el tamaño fijo de la cola circular.
    front: Un entero que indica el índice del primer elemento en la cola. Inicialmente se establece en -1, lo que indica que la cola está vacía.
    rear: Un entero que indica el índice del último elemento en la cola. También se inicializa en -1.
    queue: Un array de enteros que almacena los elementos de la cola. Su tamaño se establece por el parámetro size en el constructor.

 */
public class CircularQueue {
    private int size, front, rear;
    private int[] queue;

    public CircularQueue(int size) {
        this.size = size;
        this.queue = new int[size];
        this.front = -1;
        this.rear = -1;
    }

    // Método para verificar si la cola está vacía
    public boolean isEmpty() {
        return front == -1;
    }

    /* Método para verificar si la cola está llena
    * Comprueba si el índice siguiente a rear es igual a front.
    */
    public boolean isFull() {
        return (rear + 1) % size == front;
    }

    // Método para agregar un elemento a la cola
    public void enqueue(int element) {
        if (isFull()) {
            System.out.println("La cola está llena");
        } else {
            if (isEmpty()) {
                front = 0;
            }
            rear = (rear + 1) % size;
            queue[rear] = element;
            System.out.println("Insertado: " + element);
        }
    }

    /**
     * Elimina y retorna el elemento en front. 
     * Si la cola está vacía, muestra un mensaje de error. 
     * Si front y rear son iguales, significa que hay un solo elemento, por lo que se restablecen a -1. 
     * De lo contrario, se actualiza front al siguiente índice.
     * @return 
     */
    public int dequeue() {
        int element;
        if (isEmpty()) {
            System.out.println("La cola está vacía");
            return -1;
        } else {
            element = queue[front];
            if (front == rear) {
                front = -1;
                rear = -1;
            } else {
                front = (front + 1) % size;
            }
            return element;
        }
    }

    // Método para mostrar los elementos de la cola
    public void displayQueue() {
        if (isEmpty()) {
            System.out.println("La cola está vacía");
        } else {
            System.out.print("Elementos en la cola circular: ");
            for (int i = front; i != rear; i = (i + 1) % size) {
                System.out.print(queue[i] + " ");
            }
            System.out.println(queue[rear]);
        }
    }
}