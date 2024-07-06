/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9.lista_enlazada_circular;

/**
 *
 * @author desarrollo
 */
public class PlaylistApp {
    public static void main(String[] args) {
        CircularLinkedList playlist = new CircularLinkedList();

        // Agregar canciones a la lista de reproducción
        playlist.add("Song 1");
        playlist.add("Song 2");
        playlist.add("Song 3");
        playlist.display(); // Salida: Song 1 Song 2 Song 3

        // Agregar una canción al inicio de la lista de reproducción
        playlist.addFirst("Intro");
        playlist.display(); // Salida: Intro Song 1 Song 2 Song 3

        // Eliminar una canción de la lista de reproducción
        playlist.remove("Song 2");
        playlist.display(); // Salida: Intro Song 1 Song 3

        // Mostrar el tamaño de la lista de reproducción
        System.out.println("Tamaño de la lista: " + playlist.size()); // Output: 3
    }
}