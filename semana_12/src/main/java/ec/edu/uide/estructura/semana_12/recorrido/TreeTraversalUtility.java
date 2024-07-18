/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12.recorrido;

/**
 *
 * @author desarrollo
 */
import javax.swing.JTextArea;

public class TreeTraversalUtility {

    /**
     * Realiza un recorrido en orden (in-order) de un árbol binario y muestra los datos en un JTextArea.
     * En un recorrido en orden, primero se visita el subárbol izquierdo, luego el nodo actual y, finalmente, el subárbol derecho.
     *
     * @param root       El nodo raíz del árbol binario.
     * @param outputArea El área de texto donde se mostrarán los resultados del recorrido.
     * @param <T>        El tipo de datos que el árbol binario almacena, que debe implementar Comparable.
     */
    public static <T extends Comparable<T>> void inOrderTraversal(TreeNode<T> root, JTextArea outputArea) {
        if (root != null) {
            // Recorrido en orden del subárbol izquierdo
            inOrderTraversal(root.left, outputArea);
            // Procesa el nodo actual
            outputArea.append(root.data + " ");
            // Recorrido en orden del subárbol derecho
            inOrderTraversal(root.right, outputArea);
        }
    }

    /**
     * Realiza un recorrido en preorden (pre-order) de un árbol binario y muestra los datos en un JTextArea.
     * En un recorrido en preorden, primero se visita el nodo actual, luego el subárbol izquierdo y, finalmente, el subárbol derecho.
     *
     * @param root       El nodo raíz del árbol binario.
     * @param outputArea El área de texto donde se mostrarán los resultados del recorrido.
     * @param <T>        El tipo de datos que el árbol binario almacena, que debe implementar Comparable.
     */
    public static <T extends Comparable<T>> void preOrderTraversal(TreeNode<T> root, JTextArea outputArea) {
        if (root != null) {
            // Procesa el nodo actual
            outputArea.append(root.data + " ");
            // Recorrido en preorden del subárbol izquierdo
            preOrderTraversal(root.left, outputArea);
            // Recorrido en preorden del subárbol derecho
            preOrderTraversal(root.right, outputArea);
        }
    }

    /**
     * Realiza un recorrido en postorden (post-order) de un árbol binario y muestra los datos en un JTextArea.
     * En un recorrido en postorden, primero se visita el subárbol izquierdo, luego el subárbol derecho y, finalmente, el nodo actual.
     *
     * @param root       El nodo raíz del árbol binario.
     * @param outputArea El área de texto donde se mostrarán los resultados del recorrido.
     * @param <T>        El tipo de datos que el árbol binario almacena, que debe implementar Comparable.
     */
    public static <T extends Comparable<T>> void postOrderTraversal(TreeNode<T> root, JTextArea outputArea) {
        if (root != null) {
            // Recorrido en postorden del subárbol izquierdo
            postOrderTraversal(root.left, outputArea);
            // Recorrido en postorden del subárbol derecho
            postOrderTraversal(root.right, outputArea);
            // Procesa el nodo actual
            outputArea.append(root.data + " ");
        }
    }
}

