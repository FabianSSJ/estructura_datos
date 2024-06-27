/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semena_9;

import java.util.Scanner;

/**
 *
 * @author desarrollo
 * Sistema de Turnos en una Clínica
 * Para este caso, implementaremos un sistema que maneje los turnos de los pacientes en una clínica. 
 * Cada paciente recibe un número de turno, y el sistema debe permitir agregar pacientes a la cola 
 * de espera y atenderlos en el orden en que llegaron.
 */
public class ClinicQueueSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CircularQueue queue = new CircularQueue(5); // Tamaño de la cola

        while (true) {
            System.out.println("Sistema de Turnos de la Clínica");
            System.out.println("1. Agregar paciente a la cola");
            System.out.println("2. Atender paciente");
            System.out.println("3. Mostrar cola de pacientes");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Ingrese el número de turno del paciente: ");
                    int turnNumber = scanner.nextInt();
                    queue.enqueue(turnNumber);
                    break;
                case 2:
                    int attendedPatient = queue.dequeue();
                    if (attendedPatient != -1) {
                        System.out.println("Paciente con número de turno " + attendedPatient + " ha sido atendido.");
                    }
                    break;
                case 3:
                    queue.displayQueue();
                    break;
                case 4:
                    System.out.println("Saliendo del sistema...");
                    scanner.close();
                    System.exit(0);
                default:
                    System.out.println("Opción inválida, por favor intente de nuevo.");
            }
        }
    }
}