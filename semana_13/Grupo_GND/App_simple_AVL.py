import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

class AVLVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("AVL Tree Visualizer")
        self.tree = AVLTree()
        self.avl_root = None

        self.label = ttk.Label(root, text="Ingrese un valor:", font=('Arial', 12))
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, font=('Arial', 12))
        self.entry.pack(pady=5)

        self.insert_button = ttk.Button(root, text="Insertar", command=self.insert_node, style='TButton')
        self.insert_button.pack(pady=10)

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=6)
        style.configure('TLabel', font=('Arial', 12))
        
        self.canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0")
        self.canvas.pack(pady=20)

    def insert_node(self):
        key = int(self.entry.get())
        self.avl_root = self.tree.insert(self.avl_root, key)
        self.entry.delete(0, tk.END)
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        self.draw_node(self.avl_root, 300, 20, 100, is_root=True)

    def draw_node(self, node, x, y, dx, is_root=False):
        if node:
            color = "#FF6347" if is_root else "#87CEFA"
            outline_color = "#4682B4" if is_root else "#4682B4"
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline=outline_color, width=2)
            self.canvas.create_text(x, y, text=str(node.key), font=('Arial', 12, 'bold'), fill=outline_color)
            if node.left:
                self.canvas.create_line(x, y, x-dx, y+60, fill=outline_color, width=2)
                self.draw_node(node.left, x-dx, y+60, dx//2)
            if node.right:
                self.canvas.create_line(x, y, x+dx, y+60, fill=outline_color, width=2)
                self.draw_node(node.right, x+dx, y+60, dx//2)

if __name__ == "__main__":
    root = tk.Tk()
    app = AVLVisualizer(root)
    root.mainloop()
