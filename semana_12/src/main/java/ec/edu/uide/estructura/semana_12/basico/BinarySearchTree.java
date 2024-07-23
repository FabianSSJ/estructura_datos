/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12.basico;

import ec.edu.uide.estructura.semana_12.basico.Node;

/**
 *
 * @author desarrollo
 */
// Clase Árbol Binario de Búsqueda
public class BinarySearchTree<T extends Comparable<T>> {

    private Node<T> root;

    // Constructor
    public BinarySearchTree() {
        this.root = null;
    }

    // Método para insertar un dato en el árbol
    public void insert(T data) {
        root = insertRec(root, data);
    }

    // Método recursivo para insertar un dato en el árbol
    private Node<T> insertRec(Node<T> root, T data) {
        // Si el árbol está vacío, crear un nuevo nodo
        if (root == null) {
            root = new Node<>(data);
            return root;
        }

        // De lo contrario, recorrer el árbol
        if (data.compareTo(root.data) < 0) {
            root.left = insertRec(root.left, data);
        } else if (data.compareTo(root.data) > 0) {
            root.right = insertRec(root.right, data);
        }

        // Devolver el nodo no modificado
        return root;
    }

    // Método para buscar un dato en el árbol
    public boolean search(T data) {
        return searchRec(root, data);
    }

    // Método recursivo para buscar un dato en el árbol
    private boolean searchRec(Node<T> root, T data) {
        // Caso base: el nodo es nulo o el dato está presente en el nodo
        if (root == null || root.data.equals(data)) {
            return root != null;
        }

        // El dato es mayor que el dato de la raíz
        if (data.compareTo(root.data) < 0) {
            return searchRec(root.left, data);
        }

        // El dato es menor que el dato de la raíz
        return searchRec(root.right, data);
    }

    // Método para eliminar un dato del árbol
    public void delete(T data) {
        root = deleteRec(root, data);
    }

    // Método recursivo para eliminar un dato del árbol
    private Node<T> deleteRec(Node<T> root, T data) {
        // Caso base: el árbol está vacío
        if (root == null) {
            return root;
        }

        // Recorrer el árbol
        if (data.compareTo(root.data) < 0) {
            root.left = deleteRec(root.left, data);
        } else if (data.compareTo(root.data) > 0) {
            root.right = deleteRec(root.right, data);
        } else {
            // Nodo con solo un hijo o sin hijos
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Nodo con dos hijos: obtener el sucesor en orden (el más pequeño en el subárbol derecho)
            root.data = minValue(root.right);

            // Eliminar el sucesor en orden
            root.right = deleteRec(root.right, root.data);
        }

        return root;
    }

    // Método para encontrar el valor mínimo en un árbol
    private T minValue(Node<T> root) {
        T minValue = root.data;
        while (root.left != null) {
            minValue = root.left.data;
            root = root.left;
        }
        return minValue;
    }

    // Método para realizar un recorrido en orden del árbol
    public void inOrderTraversal() {
        inOrderRec(root);
    }

    // Método recursivo para realizar un recorrido en orden del árbol
    private void inOrderRec(Node<T> root) {
        if (root != null) {
            inOrderRec(root.left);
            System.out.print(root.data + " ");
            inOrderRec(root.right);
        }
    }
}