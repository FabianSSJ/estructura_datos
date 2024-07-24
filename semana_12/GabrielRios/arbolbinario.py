class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)
        return result

    def evaluate_expression(self, node):
        if node:
            if node.val.isdigit():
                return int(node.val)
            else:
                left_val = self.evaluate_expression(node.left)
                right_val = self.evaluate_expression(node.right)
                if node.val == '+':
                    return left_val + right_val
                elif node.val == '-':
                    return left_val - right_val
                elif node.val == '*':
                    return left_val * right_val
                elif node.val == '/':
                    return left_val / right_val

# Ejemplo de uso:
# Construcción del árbol de expresión para la expresión: (3 + (2 * 5))

root = Node('+')
root.left = Node('3')
root.right = Node('*')
root.right.left = Node('2')
root.right.right = Node('5')

tree = BinaryTree()
tree.root = root

# Recorridos
print("Inorden:", tree.inorder_traversal(tree.root, []))
print("Preorden:", tree.preorder_traversal(tree.root, []))
print("Postorden:", tree.postorder_traversal(tree.root, []))

# Evaluación de la expresión
print("Evaluación de la expresión:", tree.evaluate_expression(tree.root))
