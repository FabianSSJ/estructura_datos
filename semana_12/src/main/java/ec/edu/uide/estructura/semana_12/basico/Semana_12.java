/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package ec.edu.uide.estructura.semana_12.basico;

import ec.edu.uide.estructura.semana_12.basico.BinarySearchTree;

/**
 *
 * @author desarrollo
 */
public class Semana_12 {

    public static void main(String[] args) {
        BinarySearchTree<Integer> bst = new BinarySearchTree<>();

        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);

        // Recorrido en orden
        System.out.println("Recorrido en orden:");
        bst.inOrderTraversal();
        System.out.println();

        // Buscar un elemento
        System.out.println("Buscar 40: " + bst.search(40)); // true
        System.out.println("Buscar 90: " + bst.search(90)); // false

        // Eliminar un elemento
        bst.delete(20);
        System.out.println("Recorrido en orden después de eliminar 20:");
        bst.inOrderTraversal();
        System.out.println();

        bst.delete(30);
        System.out.println("Recorrido en orden después de eliminar 30:");
        bst.inOrderTraversal();
        System.out.println();

        bst.delete(50);
        System.out.println("Recorrido en orden después de eliminar 50:");
        bst.inOrderTraversal();
        System.out.println();
    }
}
