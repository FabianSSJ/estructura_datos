class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._add_node(key, self.root)

    def _add_node(self, key, node):
        if key < node.key:
            if node.left_child is None:
                node.left_child = TreeNode(key)
            else:
                self._add_node(key, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = TreeNode(key)
            else:
                self._add_node(key, node.right_child)

    def find(self, key):
        return self._find_node(key, self.root)

    def _find_node(self, key, node):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find_node(key, node.left_child)
        else:
            return self._find_node(key, node.right_child)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left_child, result)
            result.append(node.key)
            self.inorder(node.right_child, result)
        return result

    def preorder(self, node, result):
        if node:
            result.append(node.key)
            self.preorder(node.left_child, result)
            self.preorder(node.right_child, result)
        return result

    def postorder(self, node, result):
        if node:
            self.postorder(node.left_child, result)
            self.postorder(node.right_child, result)
            result.append(node.key)
        return result

# Creación del árbol binario y almacenamiento de términos
bst = BinarySearchTree()
items = ["nota", "esfero", "melancolia", "luna", "ventana", "oscuridad", "montaña"]

for item in items:
    bst.add(item)

# Búsqueda de términos
search_items = ["nota", "melancolia", "montaña"]
for item in search_items:
    found = bst.find(item)
    print(f"Item '{item}': {'Found' if found else 'Not found'}")

# Recorridos del árbol
print("Inorder traversal:", bst.inorder(bst.root, []))
print("Preorder traversal:", bst.preorder(bst.root, []))
print("Postorder traversal:", bst.postorder(bst.root, []))





