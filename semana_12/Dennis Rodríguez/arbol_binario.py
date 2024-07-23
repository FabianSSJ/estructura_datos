class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

def evaluate(node):
    if node.left is None and node.right is None:
        return int(node.value)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

# Ejemplo de uso
if __name__ == "__main__":
    # Construcción del árbol de expresión para 3 + (2 * 5)
    root = Node('+')
    root.left = Node('3')
    root.right = Node('*')
    root.right.left = Node('2')
    root.right.right = Node('5')

    # Evaluación de la expresión aritmética
    result = evaluate(root)
    print(f"Resultado de la expresión: {result}")

    # Recorridos del árbol
    tree = BinaryTree()
    tree.root = root

    inorder_result = []
    tree.inorder(tree.root, inorder_result)
    print(f"Recorrido Inorden: {inorder_result}")

    preorder_result = []
    tree.preorder(tree.root, preorder_result)
    print(f"Recorrido Preorden: {preorder_result}")

    postorder_result = []
    tree.postorder(tree.root, postorder_result)
    print(f"Recorrido Postorden: {postorder_result}")
