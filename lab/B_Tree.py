class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree

    def insert(self, key):
        root = self.root

        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            new_root.children.append(self.root)
            self.root = new_root
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _insert_non_full(self, x, key):
        i = len(x.keys) - 1

        if x.leaf:
            x.keys.append(None)
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1

            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], key)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:2 * t - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t]

    def search(self, key, x=None):
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1

        if i < len(x.keys) and key == x.keys[i]:
            return True
        elif x.leaf:
            return False
        else:
            return self.search(key, x.children[i])

    def print_tree(self, x=None, level=0):
        if x is None:
            x = self.root

        print("Level", level, end=": ")
        print(x.keys)

        level += 1
        if len(x.children) > 0:
            for child in x.children:
                self.print_tree(child, level)

# Example usage:
if __name__ == '__main__':
    b_tree = BTree(3)  # Create a B-tree with a minimum degree of 3.

    keys = [3, 7, 1, 5, 9, 2, 6, 4, 8]
    for key in keys:
        b_tree.insert(key)

    print("B-tree structure:")
    b_tree.print_tree()

    search_key = 6
    if b_tree.search(search_key):
        print(f"Key {search_key} is in the B-tree.")
    else:
        print(f"Key {search_key} is not in the B-tree.")
