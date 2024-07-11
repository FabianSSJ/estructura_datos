class Nodo {
    String nombre;
    int tiempoLlegada;
    Nodo siguiente;
    Nodo anterior;

    public Nodo(String nombre, int tiempoLlegada) {
        this.nombre = nombre;
        this.tiempoLlegada = tiempoLlegada;
        this.siguiente = null;
        this.anterior = null;
    }
}

class ColaDobleEnlace {
    Nodo primerNodo;  // Primer nodo de la cola
    Nodo ultimoNodo;  // Último nodo de la cola

    public ColaDobleEnlace() {
        this.primerNodo = null;
        this.ultimoNodo = null;
    }

    // Método para encolar un nuevo cliente
    public void encolar(String nombre, int tiempoLlegada) {
        Nodo nuevoNodo = new Nodo(nombre, tiempoLlegada);
        if (ultimoNodo == null) {
            primerNodo = nuevoNodo;
            ultimoNodo = nuevoNodo;
        } else {
            ultimoNodo.siguiente = nuevoNodo;
            nuevoNodo.anterior = ultimoNodo;
            ultimoNodo = nuevoNodo;
        }
    }

    // Método para desencolar y obtener el próximo cliente a atender
    public Nodo desencolar() {
        if (primerNodo == null) {
            return null;  // La cola está vacía
        } else {
            Nodo nodoAAtender = primerNodo;
            primerNodo = primerNodo.siguiente;
            if (primerNodo != null) {
                primerNodo.anterior = null;
            } else {
                ultimoNodo = null;  // Si el primerNodo era el único elemento
            }
            return nodoAAtender;
        }
    }

    // Método para verificar si la cola está vacía
    public boolean estaVacia() {
        return primerNodo == null;
    }
}

public class SimulacionCola{

    // Función para simular la atención de clientes
    public static void simularAtencionClientes() {
        ColaDobleEnlace colaClientes = new ColaDobleEnlace();

        // Simular la llegada de clientes
        colaClientes.encolar("Jose", 3);  // Cliente 1 llega en el tiempo 3
        colaClientes.encolar("Pedro", 1);  // Cliente 2 llega en el tiempo 1
        colaClientes.encolar("Juan", 2);  // Cliente 3 llega en el tiempo 2

        System.out.println("Clientes en cola:");
        System.out.println("-----------------");
        System.out.println("Nombre\t\tTiempo de Llegada");
        System.out.println("------\t\t----------------");

        // Mostrar los clientes en cola
        Nodo nodoActual = colaClientes.primerNodo;
        while (nodoActual != null) {
            System.out.println(nodoActual.nombre + "\t\t" + nodoActual.tiempoLlegada);
            nodoActual = nodoActual.siguiente;
        }

        System.out.println("\nAtendiendo a los clientes:");
        System.out.println("--------------------------");

        // Atender a los clientes en el orden de llegada
        while (!colaClientes.estaVacia()) {
            Nodo cliente = colaClientes.desencolar();
            if (cliente != null) {
                System.out.println("Atendiendo a " + cliente.nombre + " (Tiempo de Llegada: " + cliente.tiempoLlegada + ")");
                // Simular el proceso de atención (aquí se puede agregar una pausa para simular el tiempo de atención)
            }
        }

        System.out.println("\nTodos los clientes han sido atendidos.");
    }

    public static void main(String[] args) {
        simularAtencionClientes();
    }
}
