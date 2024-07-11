class Nodo {
    String dato;
    Nodo previo;
    Nodo siguiente;

    public Nodo(String dato) {
        this.dato = dato;
        this.previo = null;
        this.siguiente = null;
    }
}

class ColaListaDoble {
    private Nodo frente;
    private Nodo fondo;

    public ColaListaDoble() {
        this.frente = null;
        this.fondo = null;
    }

    public boolean estaVacia() {
        return frente == null;
    }

    public void encolar(String dato) {
        Nodo nuevoNodo = new Nodo(dato);
        if (estaVacia()) {
            frente = fondo = nuevoNodo;
        } else {
            fondo.siguiente = nuevoNodo;
            nuevoNodo.previo = fondo;
            fondo = nuevoNodo;
        }
    }

    public String desencolar() {
        if (estaVacia()) {
            throw new RuntimeException("La cola está vacía");
        }
        String dato = frente.dato;
        frente = frente.siguiente;
        if (frente != null) {
            frente.previo = null;
        } else {
            fondo = null;
        }
        return dato;
    }

    public void imprimirCola() {
        if (estaVacia()) {
            System.out.println("La cola está vacía");
            return;
        }
        Nodo actual = frente;
        while (actual != null) {
            System.out.print(actual.dato + " ");
            actual = actual.siguiente;
        }
        System.out.println();
    }
}

class Cliente {
    String nombre;
    long tiempoLlegada;

    public Cliente(String nombre, long tiempoLlegada) {
        this.nombre = nombre;
        this.tiempoLlegada = tiempoLlegada;
    }
}

public class list2Enlazada {
    public static void main(String[] args) {
        ColaListaDoble cola = new ColaListaDoble();
        Random random = new Random();

        // Simulación de llegada de clientes
        for (int i = 1; i <= 10; i++) {
            String nombre = "Cliente " + i;
            long tiempoLlegada = System.currentTimeMillis() + random.nextInt(1000);
            Cliente cliente = new Cliente(nombre, tiempoLlegada);
            cola.encolar(cliente.nombre);
            System.out.println("Llegó " + cliente.nombre + " a las " + cliente.tiempoLlegada);
        }


        // Simulación de atención de clientess
        System.out.println("\nAtendiendo clientes...");
        while (!cola.estaVacia()) {
            String clienteAtendido = cola.desencolar();
            System.out.println("Atendiendo a " + clienteAtendido + " a las " + System.currentTimeMillis());
            try {
                Thread.sleep(500); // Simular tiempo de atención
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
