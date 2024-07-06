/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.arreglos_dinamicos;

import java.util.ArrayList;

/**
 *
 * @author desarrollo
 */
public class ArrayListExample {

    public static void main(String[] args) {
        // Crear un ArrayList de enteros
        ArrayList<Integer   > numbers = new ArrayList<>();

        // Agregar elementos al ArrayList
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        System.out.println("ArrayList antes de agregar elementos: " + numbers);

        // Obtener un elemento en una posición específica
        int numberAtIndex1 = numbers.get(1);
        System.out.println("Elemento en la posición 1: " + numberAtIndex1);

        // Modificar un elemento en una posición específica
        numbers.set(1, 50);
        System.out.println("ArrayList despues de actulizar elmento en la posición: " + numbers);

        // Eliminar un elemento en una posición específica
        numbers.remove(2);
        System.out.println("ArrayList despues de eliminar elemento en la posición 2: " + numbers);

        // Verificar el tamaño del ArrayList
        int size = numbers.size();
        System.out.println("Tamaño del ArrayList: " + size);

        // Verificar si el ArrayList contiene un elemento específico
        boolean contains20 = numbers.contains(20);
        System.out.println("ArrayList contiene elemento 20?: " + contains20);

        // Recorrer el ArrayList
        System.out.println("Elemenios en ArrayList:");
        for (int number : numbers) {
            System.out.println(number);
        }
    }
}
