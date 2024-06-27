/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.lista_enlazada_doble_circular;

/**
 *
 * @author desarrollo
 */
public class RestaurantOrderSystem {
    public static void main(String[] args) {
        DoublyCircularLinkedList orderList = new DoublyCircularLinkedList();

        // Agregar pedidos a la lista
        orderList.add(1);
        orderList.add(2);
        orderList.add(3);
        orderList.add(4);

        // Mostrar todos los pedidos
        orderList.display(); // Output: 1 2 3 4

        // Agregar pedido al inicio de la lista
        orderList.addFirst(0);
        orderList.display(); // Output: 0 1 2 3 4

        // Eliminar un pedido de la lista
       // orderList.remove(2);
        orderList.display(); // Output: 0 1 3 4

        // Mostrar la lista en orden inverso
        orderList.displayReverse(); // Output: 4 3 1 0

        // Mostrar el tamaño de la lista de pedidos
        System.out.println("Número de pedidos en la lista: " + orderList.size()); // Output: 4
    }
}
