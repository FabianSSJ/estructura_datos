/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_11;

/**
 *
 * @author desarrollo
 */
public class CheckPalindrome extends ConsoleProgram {

    public String removeSpaces(String text) {
        return text.replaceAll("\\s", "");
    }
    
    public String preprocessText(String text) {
        // Remove all non-alphanumeric characters and convert to lowercase
        return text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    }

    public boolean isPalindrome(String text) {
        int left = 0;
        int right = text.length() - 1;
    
        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public void run() {
        String text = readLine("Enter text to check: ");
        text = preprocessText(text);
        if (isPalindrome(text)) {
            println("Text is palindrome.");
        } else {
            println("Text is not palindrome.");
        }
    }

    public static void main(String[] args) {
        new CheckPalindrome().run();
    }
    
    
    
}
