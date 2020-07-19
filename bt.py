from queue import Queue
from Stack import Stack


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BT(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")

        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")

        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")

        elif traversal_type == "level order":
            return self.level_order(tree.root)

        elif traversal_type == "reverse level order":
            return self.reverse_level_order(tree.root)

        else:
            print("traversal type " + str(traversal_type) + " is not supported ")
            return False

    def preorder(self, start, traversal):
        if start:
            traversal += str(start.data) + "-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.data) + "-"
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.data) + "-"

        return traversal

    def level_order(self, start):
        if not start:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += str((queue.peek()).data) + "-"

            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def size(self):
        start = self.root

        if not start:
            return 0

        queue = Queue()
        queue.enqueue(start)

        count = 0
        while len(queue) > 0:

            count += 1
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return count

    def reverse_level_order(self, start):

        if not start:
            return

        queue = Queue()
        queue.enqueue(start)

        s = Stack()

        traversal = ""

        while len(queue) > 0:

            node = queue.dequeue()
            s.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while not s.isEmpty():

            node = s.pop()
            traversal += str(node.data) + "-"

        return traversal

    def max(self, left, right):
        if left > right:
            return left
        else:
            return right

    def height(self, node):

        node = node
        if not node:
            return -1

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return 1 + self.max(height_left, height_right)


tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("level order"))
print(tree.print_tree("reverse level order"))
print(tree.height(tree.root))
print("Size ", tree.size())
