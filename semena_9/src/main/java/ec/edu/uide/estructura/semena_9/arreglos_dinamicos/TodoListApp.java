/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.arreglos_dinamicos;

/**
 *
 * @author desarrollo
 * Gestión de una lista de tareas pendientes (to-do list)
 */
public class TodoListApp {
    public static void main(String[] args) {
        DynamicArray todoList = new DynamicArray(2);

        // Agregar tareas a la lista
        todoList.add(1); // Tarea 1
        todoList.add(2); // Tarea 2
        System.out.println("Lista de tareas después de agregar 2 tareas:");
        todoList.display();

        // Agregar otra tarea para ver la redimensión del arreglo
        todoList.add(3); // Tarea 3
        System.out.println("Lista de tareas después de agregar una tercera tarea:");
        todoList.display();
        

        // Eliminar una tarea de la lista
        todoList.remove(1); // Eliminar tarea en índice 1 (segunda tarea)
        System.out.println("Lista de tareas después de eliminar la tarea en índice 1:");
        todoList.display();
        
        todoList.add(4); // Tarea 3
        todoList.add(5); // Tarea 3
        todoList.add(6); // Tarea 3
        todoList.add(7); // Tarea 3
        
        todoList.display();

        // Obtener y mostrar una tarea en un índice específico
        System.out.println("Tarea en índice 1: " + todoList.get(1));

        // Mostrar el tamaño y la capacidad del arreglo
        System.out.println("Tamaño de la lista de tareas: " + todoList.size());
        System.out.println("Capacidad de la lista de tareas: " + todoList.capacity());
    }
}