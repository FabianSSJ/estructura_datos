/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ec.edu.uide.estructura.semana_12;

/**
 *
 * @author desarrollo
 */
import javax.swing.*;
import java.awt.*;

class TreePanel extends JPanel {

    private BinarySearchTreeV2<Integer> bst;

    public TreePanel(BinarySearchTreeV2<Integer> bst) {
        this.bst = bst;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (bst.getRoot() != null) {
            drawTree(g, getWidth() / 2, 30, bst.getRoot(), getWidth() / 4);
        }
    }

    private void drawTree(Graphics g, int x, int y, Node<Integer> node, int xOffset) {
        if (node == null) {
            return;
        }

        g.setColor(Color.BLACK);
        g.fillOval(x - 15, y - 15, 30, 30);
        g.setColor(Color.WHITE);
        g.drawString(node.data.toString(), x - 10, y + 4);

        if (node.left != null) {
            g.setColor(Color.RED);
            g.drawLine(x - 5, y + 5, x - xOffset + 5, y + 50 - 5);
            drawTree(g, x - xOffset, y + 50, node.left, xOffset / 2);
        }

        if (node.right != null) {
            g.setColor(Color.BLUE);
            g.drawLine(x + 5, y + 5, x + xOffset - 5, y + 50 - 5);
            drawTree(g, x + xOffset, y + 50, node.right, xOffset / 2);
        }
    }
}
