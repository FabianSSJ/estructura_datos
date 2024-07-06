/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.arreglos_dinamicos;

import java.util.Arrays;

/**
 *
 * @author desarrollo
 */
public class DynamicArray {
    private int[] array;
    private int size;
    private int capacity;

    // Constructor
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.array = new int[capacity];
        this.size = 0;
    }

    // Método para agregar un elemento
    public void add(int element) {
        if (size == capacity) {
            resize();
        }
        array[size++] = element;
    }

    // Método para redimensionar el arreglo
    // Duplica la capacidad del arreglo cuando se alcanza la capacidad actual.
    private void resize() {
        capacity *= 2;
        array = Arrays.copyOf(array, capacity);
    }

    // Método para obtener un elemento en una posición específica
    public int get(int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        return array[index];
    }

    // Método para eliminar un elemento en una posición específica
    public void remove(int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
        }
        for (int i = index; i < size - 1; i++) {
            array[i] = array[i + 1];
        }
        array[--size] = 0; // Opcional: limpiar el último elemento
    }

    // Método para obtener el tamaño actual del arreglo
    public int size() {
        return size;
    }

    // Método para obtener la capacidad actual del arreglo
    public int capacity() {
        return capacity;
    }

    // Método para mostrar los elementos del arreglo
    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
}