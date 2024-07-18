/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12;

/**
 *
 * @author desarrollo
 */
import java.util.Stack;

public class BinarySearchTreeIterative<T extends Comparable<T>> {
    // Nodo raíz del árbol binario de búsqueda
    private Node<T> root;

    // Constructor que inicializa el árbol vacío
    public BinarySearchTreeIterative() {
        this.root = null;
    }

    // Método para obtener la raíz del árbol
    public Node<T> getRoot() {
        return root;
    }

    // Método público para insertar un dato en el árbol
    public void insert(T data) {
        Node<T> newNode = new Node<>(data);
        if (root == null) {
            root = newNode;
            return;
        }

        Node<T> current = root;
        Node<T> parent = null;

        while (true) {
            parent = current;
            if (data.compareTo(current.data) < 0) {
                current = current.left;
                if (current == null) {
                    parent.left = newNode;
                    return;
                }
            } else {
                current = current.right;
                if (current == null) {
                    parent.right = newNode;
                    return;
                }
            }
        }
    }

    // Método público para buscar un dato en el árbol
    public boolean search(T data) {
        Node<T> current = root;
        while (current != null) {
            if (data.compareTo(current.data) == 0) {
                return true;
            } else if (data.compareTo(current.data) < 0) {
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return false;
    }

    // Método público para eliminar un dato del árbol
    public void delete(T data) {
        root = deleteNode(root, data);
    }

    // Método para eliminar un nodo utilizando bucles
    private Node<T> deleteNode(Node<T> root, T data) {
        Node<T> parent = null;
        Node<T> current = root;

        while (current != null && current.data.compareTo(data) != 0) {
            parent = current;
            if (data.compareTo(current.data) < 0) {
                current = current.left;
            } else {
                current = current.right;
            }
        }

        if (current == null) {
            return root; // Nodo no encontrado
        }

        // Nodo con dos hijos
        if (current.left != null && current.right != null) {
            Node<T> successor = findMin(current.right);
            T val = successor.data;
            delete(val);
            current.data = val;
        } else {
            // Nodo con un solo hijo o sin hijos
            Node<T> child = (current.left != null) ? current.left : current.right;

            if (parent == null) {
                return child;
            }

            if (current == parent.left) {
                parent.left = child;
            } else {
                parent.right = child;
            }
        }
        return root;
    }

    // Método para encontrar el valor mínimo en el subárbol
    private Node<T> findMin(Node<T> node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    // Método público para realizar un recorrido en orden del árbol
    public void inOrderTraversal() {
        if (root == null) {
            return;
        }

        Node<T> current = root;
        Stack<Node<T>> stack = new Stack<>();

        while (current != null || !stack.isEmpty()) {
            while (current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            System.out.print(current.data + " ");
            current = current.right;
        }
    }

    // Clase anidada para representar los nodos del árbol
    static class Node<T> {
        T data;
        Node<T> left, right;

        public Node(T item) {
            data = item;
            left = right = null;
        }
    }

    public static void main(String[] args) {
        BinarySearchTreeIterative<Integer> bst = new BinarySearchTreeIterative<>();
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);

        System.out.println("Recorrido en orden:");
        bst.inOrderTraversal(); // Salida esperada: 20 30 40 50 60 70 80

        System.out.println("\nBuscar 40: " + bst.search(40)); // Salida esperada: true
        System.out.println("Buscar 90: " + bst.search(90)); // Salida esperada: false

        System.out.println("Eliminar 20");
        bst.delete(20);
        System.out.println("Recorrido en orden:");
        bst.inOrderTraversal(); // Salida esperada: 30 40 50 60 70 80

        System.out.println("\nEliminar 30");
        bst.delete(30);
        System.out.println("Recorrido en orden:");
        bst.inOrderTraversal(); // Salida esperada: 40 50 60 70 80

        System.out.println("\nEliminar 50");
        bst.delete(50);
        System.out.println("Recorrido en orden:");
        bst.inOrderTraversal(); // Salida esperada: 40 60 70 80
    }
}