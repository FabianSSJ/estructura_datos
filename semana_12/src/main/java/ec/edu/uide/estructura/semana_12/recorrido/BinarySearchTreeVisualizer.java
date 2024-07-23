/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12.recorrido;

/**
 *
 * @author desarrollo
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BinarySearchTreeVisualizer extends JFrame {

    private BinarySearchTree<Integer> binarySearchTree;
    private JTextArea outputArea;

    public BinarySearchTreeVisualizer() {
        binarySearchTree = new BinarySearchTree<>();
        binarySearchTree.insert(50);
        binarySearchTree.insert(30);
        binarySearchTree.insert(20);
        binarySearchTree.insert(40);
        binarySearchTree.insert(70);
        binarySearchTree.insert(60);
        binarySearchTree.insert(80);
        binarySearchTree.insert(100);
        binarySearchTree.insert(61);
        binarySearchTree.insert(62);
        
        binarySearchTree.insert(10);
        binarySearchTree.insert(45);
        
        binarySearchTree.insert(2);
        
        binarySearchTree.insert(5);
        binarySearchTree.insert(1);
        

        setTitle("Visualizador de Árbol Binario de Búsqueda");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        outputArea = new JTextArea(5, 20);
        outputArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(outputArea);

        JPanel buttonPanel = new JPanel();
        JButton inOrderButton = new JButton("In-Order");
        JButton preOrderButton = new JButton("Pre-Order");
        JButton postOrderButton = new JButton("Post-Order");

        inOrderButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                outputArea.setText("");
                TreeTraversalUtility.inOrderTraversal(binarySearchTree.getRoot(), outputArea);
            }
        });

        preOrderButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                outputArea.setText("");
                TreeTraversalUtility.preOrderTraversal(binarySearchTree.getRoot(), outputArea);
            }
        });

        postOrderButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                outputArea.setText("");
                TreeTraversalUtility.postOrderTraversal(binarySearchTree.getRoot(), outputArea);
            }
        });

        buttonPanel.add(inOrderButton);
        buttonPanel.add(preOrderButton);
        buttonPanel.add(postOrderButton);

        add(buttonPanel, BorderLayout.NORTH);
        add(new TreeDrawingPanel(binarySearchTree), BorderLayout.CENTER);
        add(scrollPane, BorderLayout.SOUTH);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            BinarySearchTreeVisualizer frame = new BinarySearchTreeVisualizer();
            frame.setVisible(true);
        });
    }
}

