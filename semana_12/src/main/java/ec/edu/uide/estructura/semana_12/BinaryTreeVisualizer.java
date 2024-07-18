/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

/**
 *
 * @author desarrollo
 */
public class BinaryTreeVisualizer extends JFrame {
    private BinarySearchTreeV2<Integer> bst;

    public BinaryTreeVisualizer() {
        bst = new BinarySearchTreeV2<>();
        bst.insert(50);
        bst.insert(30);
        bst.insert(20);
        bst.insert(40);
        bst.insert(70);
        bst.insert(60);
        bst.insert(80);
        bst.insert(100);
        
        bst.insert(10);
        bst.insert(1);
        bst.insert(25);
        
        setTitle("Visualizador de árbol binario de búsqueda");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        add(new TreePanel(bst));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BinaryTreeVisualizer frame = new BinaryTreeVisualizer();
            frame.setVisible(true);
        });
    }
}
