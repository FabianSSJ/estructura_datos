/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_11;

import java.util.Scanner;

/**
 *
 * @author desarrollo
 */
import java.util.Scanner;

public abstract class ConsoleProgram {
    private Scanner scanner;

    public ConsoleProgram() {
        scanner = new Scanner(System.in);
    }

    public void println(String message) {
        System.out.println(message);
    }

    public int readInt(String prompt) {
        System.out.print(prompt);
        while (!scanner.hasNextInt()) {
            System.out.print("That's not a valid number. " + prompt);
            scanner.next(); // discard the invalid input
        }
        return scanner.nextInt();
    }

    public String readLine(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine();
    }

    public abstract void run();
}
