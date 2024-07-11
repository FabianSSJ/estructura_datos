/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_11;

/**
 *
 * @author desarrollo
 */
public class SquareRoot extends ConsoleProgram { 
    public int squareRoot(int n) {
        int lower = 0;
        while ((lower + 1) * (lower + 1) <= n) {
            lower = lower + 1; 
        }
        return lower; 
    }

    public void run() {
        int n = readInt("Enter a natural number: ");
        int root = squareRoot(n);
        println("The root is " + root); 
    }
    
    public static void main(String[] args) {
        new SquareRoot().run();
    }
}

