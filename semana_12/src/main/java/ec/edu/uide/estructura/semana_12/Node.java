/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12;

/**
 *
 * @author desarrollo
 */
// Clase Nodo
public class Node<T extends Comparable<T>> {
    public T data;
    public Node<T> left;
    public Node<T> right;

    // Constructor
    public Node(T data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
