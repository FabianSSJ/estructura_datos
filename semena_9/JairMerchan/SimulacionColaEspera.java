class Node {
    String nombre;
    int tiempoLlegada;
    Node siguiente;
    Node anterior;

    public Node(String nombre, int tiempoLlegada) {
        this.nombre = nombre;
        this.tiempoLlegada = tiempoLlegada;
        this.siguiente = null;
        this.anterior = null;
    }
}

class Queue {
    Node cabeza;  // Primer nodo de la cola
    Node cola;    // Último nodo de la cola

    public Queue() {
        this.cabeza = null;
        this.cola = null;
    }

    // Método para encolar un nuevo cliente
    public void enqueue(String nombre, int tiempoLlegada) {
        Node nuevoCliente = new Node(nombre, tiempoLlegada);
        if (cola == null) {
            cabeza = nuevoCliente;
            cola = nuevoCliente;
        } else {
            cola.siguiente = nuevoCliente;
            nuevoCliente.anterior = cola;
            cola = nuevoCliente;
        }
    }

    // Método para desencolar y obtener el próximo cliente a atender
    public Node dequeue() {
        if (cabeza == null) {
            return null;  // La cola está vacía
        } else {
            Node cliente = cabeza;
            cabeza = cabeza.siguiente;
            if (cabeza != null) {
                cabeza.anterior = null;
            } else {
                cola = null;  // Si la cabeza era el único elemento
            }
            return cliente;
        }
    }

    // Método para verificar si la cola está vacía
    public boolean isEmpty() {
        return cabeza == null;
    }
}

public class SimulacionColaEspera {

    // Función para simular la atención de clientes
    public static void simulacionColaEspera() {
        Queue colaEspera = new Queue();

        // Simular la llegada de clientes
        colaEspera.enqueue("Jose", 3);  // Cliente 1 llega en el tiempo 0
        colaEspera.enqueue("Pedro", 1);  // Cliente 2 llega en el tiempo 1
        colaEspera.enqueue("Juan", 2);  // Cliente 3 llega en el tiempo 2

        System.out.println("Clientes en cola:");
        System.out.println("-----------------");
        System.out.println("Nombre\t\tTiempo de Llegada");
        System.out.println("------\t\t----------------");

        // Mostrar los clientes en cola
        Node nodoActual = colaEspera.cabeza;
        while (nodoActual != null) {
            System.out.println(nodoActual.nombre + "\t\t" + nodoActual.tiempoLlegada);
            nodoActual = nodoActual.siguiente;
        }

        System.out.println("\nAtendiendo a los clientes:");
        System.out.println("--------------------------");

        // Atender a los clientes en el orden de llegada
        while (!colaEspera.isEmpty()) {
            Node cliente = colaEspera.dequeue();
            if (cliente != null) {
                System.out.println("Atendiendo a " + cliente.nombre + " (Tiempo de Llegada: " + cliente.tiempoLlegada + ")");
                // Simular el proceso de atención (aquí se puede agregar una pausa para simular el tiempo de atención)
            }
        }

        System.out.println("\nTodos los clientes han sido atendidos.");
    }

    public static void main(String[] args) {
        simulacionColaEspera();
    }
}
