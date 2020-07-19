from queue import Queue


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)

        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):

        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)

            else:
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)

            else:
                self._insert(data, cur_node.right)

        else:
            print("Element already exists")

    def find(self, data):

        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):

        if data == cur_node.data:
            return True

        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)

        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

    def inorder(self):
        if self.root:
            traversal = []
            self._inorder(self.root, traversal)
            return traversal

        else:
            return None

    def _inorder(self, cur_node, traversal):
        if cur_node:
            traversal = self._inorder(cur_node.left, traversal)
            traversal.append(cur_node.data)
            traversal = self._inorder(cur_node.right, traversal)

        return traversal

    def is_bst(self):
        if not self.root:
            return True

        val = self.inorder()
        for i in range(len(val)-1):
            if val[i] > val[i+1]:
                return False

        return True


b = BST()
b.insert(8)
b.insert(3)
b.insert(10)
b.insert(1)
b.insert(6)
b.insert(9)
b.insert(11)

print(b.inorder())
print(b.is_bst())
