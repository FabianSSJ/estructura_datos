/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12;

import java.util.Objects;



/**
 *
 * @author desarrollo
 */
public class BinarySearchTreeV2<T extends Comparable<T>> {

    // Nodo raíz del árbol binario de búsqueda
    private Node<T> root;

    // Constructor que inicializa el árbol vacío
    public BinarySearchTreeV2() {
        this.root = null;
    }

    // Método para obtener la raíz del árbol
    public Node<T> getRoot() {
        return root;
    }

    // Método público para insertar un dato en el árbol
    public void insert(T data) {
        root = insertRec(root, data);
    }

    // Método recursivo para insertar un dato en el árbol
    private Node<T> insertRec(Node<T> root, T data) {
        // Si el nodo raíz es nulo, crea un nuevo nodo con el dato
        if (root == null) {
            root = new Node<>(data);
            return root;
        }

        // Compara el dato con el nodo raíz y decide la dirección
        if (data.compareTo(root.data) < 0) {
            root.left = insertRec(root.left, data); // Inserta en el subárbol izquierdo
        } else if (data.compareTo(root.data) > 0) {
            root.right = insertRec(root.right, data); // Inserta en el subárbol derecho
        }

        return root;
    }

    // Método público para buscar un dato en el árbol
    public boolean search(T data) {
        return searchRec(root, data);
    }

    // Método recursivo para buscar un dato en el árbol
    private boolean searchRec(Node<T> root, T data) {
        // Si el nodo raíz es nulo o el dato es igual al del nodo raíz, devuelve true si no es nulo
        if (root == null || root.data.equals(data)) {
            return root != null;
        }

        // Compara el dato con el nodo raíz y decide la dirección
        if (data.compareTo(root.data) < 0) {
            return searchRec(root.left, data); // Busca en el subárbol izquierdo
        }

        return searchRec(root.right, data); // Busca en el subárbol derecho
    }

    // Método público para eliminar un dato del árbol
    public void delete(T data) {
        root = deleteRec(root, data);
    }

    // Método recursivo para eliminar un dato del árbol
    private Node<T> deleteRec(Node<T> root, T data) {
        // Si el nodo raíz es nulo, retorna el nodo raíz
        if (root == null) {
            return root;
        }

        // Compara el dato con el nodo raíz y decide la dirección
        if (data.compareTo(root.data) < 0) {
            root.left = deleteRec(root.left, data); // Elimina del subárbol izquierdo
        } else if (data.compareTo(root.data) > 0) {
            root.right = deleteRec(root.right, data); // Elimina del subárbol derecho
        } else {
            // Nodo encontrado, maneja los casos de eliminación
            if (root.left == null) {
                return root.right; // Si no tiene hijo izquierdo, retorna el derecho
            } else if (root.right == null) {
                return root.left; // Si no tiene hijo derecho, retorna el izquierdo
            }

            // Nodo con dos hijos, obtiene el menor valor del subárbol derecho
            root.data = minValue(root.right);
            // Elimina el menor valor encontrado en el subárbol derecho
            root.right = deleteRec(root.right, root.data);
        }

        return root;
    }

    // Método para encontrar el valor mínimo en el subárbol
    private T minValue(Node<T> root) {
        T minValue = root.data;
        while (root.left != null) {
            minValue = root.left.data;
            root = root.left;
        }
        return minValue;
    }

    // Método público para realizar un recorrido en orden del árbol
    public void inOrderTraversal() {
        inOrderRec(root);
    }

    // Método recursivo para realizar un recorrido en orden del árbol
    private void inOrderRec(Node<T> root) {
        if (root != null) {
            inOrderRec(root.left); // Recorre el subárbol izquierdo
            System.out.print(root.data + " "); // Visita el nodo raíz
            inOrderRec(root.right); // Recorre el subárbol derecho
        }
    }
    
}

