/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.richardarmijos;

/**
 *
 * @author desarrollo
 */
public class BusquedaLinealRecursiva {
    
    // Búsqueda Lineal Recursiva
    public static int linearSearch(int[] arr, int index, int x) {
        // Caso base: Si el índice supera la longitud del arreglo
        if (index >= arr.length) {
            return -1; // Elemento no encontrado
        }
        // Si el elemento en la posición actual es el buscado
        if (arr[index] == x) {
            return index; // Retornar el índice del elemento encontrado
        }
        // Llamada recursiva al siguiente elemento
        return linearSearch(arr, index + 1, x);
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 10, 40};
        int x = 10;

        // Llamada a la búsqueda lineal recursiva
        int result = linearSearch(arr, 0, x);
        if (result == -1) {
            System.out.println("Elemento no encontrado en el arreglo");
        } else {
            System.out.println("Elemento encontrado en el índice " + result);
        }
    }
    
    // comentario de prueba
}
