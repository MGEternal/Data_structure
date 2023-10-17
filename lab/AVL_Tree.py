class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        return x

    def rotateLeft(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.getMinValueNode(root.right).key
            root.right = self.delete(root.right, root.key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) >= 0:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        if balance < -1:
            if self.getBalance(root.right) <= 0:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def inOrderTraversal(self, root):
        if root is not None:
            self.inOrderTraversal(root.left)
            print(root.key, end=" ")
            self.inOrderTraversal(root.right)
    def printTree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key) + f" (Balance: {self.getBalance(root)} Height: {root.height}")
            if root.left is not None or root.right is not None:
                if root.left is not None:
                    self.printTree(root.left, level + 1, "L-- ")
                else:
                    print(" " * ((level + 1) * 4) + "L-- None")
                if root.right is not None:
                    self.printTree(root.right, level + 1, "R-- ")
                else:
                    print(" " * ((level + 1) * 4) + "R-- None")
# Example usage:
if __name__ == '__main__':
    tree = AVLTree()
    root = None

    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    
    for key in keys:
        root = tree.insert(root, key)

    print("AVL Tree Structure:")
    tree.printTree(root)

    key_to_delete = 10
    root = tree.delete(root, key_to_delete)
    
    print("\nAVL Tree Structure after deleting", key_to_delete)
    tree.printTree(root)
