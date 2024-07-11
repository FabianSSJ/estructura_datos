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
public class CheckPalindromeRecursive {

    // Método para eliminar espacios y caracteres no alfanuméricos y convertir a minúsculas
    public String preprocessText(String text) {
        return text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    }

    // Método recursivo para verificar si una cadena es un palíndromo
    public boolean isPalindrome(String text) {
        return isPalindromeRecursive(text, 0, text.length() - 1);
    }

    private boolean isPalindromeRecursive(String text, int left, int right) {
        // Caso base: si los punteros se cruzan o son iguales, es un palíndromo
        if (left >= right) {
            return true;
        }

        // Verificar los caracteres en las posiciones actuales
        if (text.charAt(left) != text.charAt(right)) {
            return false;
        }

        // Llamada recursiva moviendo los punteros hacia el centro
        return isPalindromeRecursive(text, left + 1, right - 1);
    }

    public boolean isPalindrome1(String text) {
        if (text.length() <= 1) {
            return true;
        } else {
            char first = text.charAt(0);
            char last = text.charAt(text.length() - 1);
            String inner = removeExtrems(text);
            return (first == last) && isPalindrome(inner);
        }
    }

    public String removeExtrems(String text) {
        // Verifica si la longitud del texto es mayor que 2 para evitar errores de índice
        if (text.length() <= 1) {
            return "";
        }
        // Retorna una nueva cadena sin el primer y el último carácter
        return text.substring(1, text.length() - 1);
    }

    public static void main(String[] args) {
        CheckPalindromeRecursive checker = new CheckPalindromeRecursive();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter text to check: ");
        String text = scanner.nextLine();

        text = checker.preprocessText(text);

        if (checker.isPalindrome1(text)) {
            System.out.println("Text is palindrome.");
        } else {
            System.out.println("Text is not palindrome.");
        }

        scanner.close();
    }
}
