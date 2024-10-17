class Child:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


class Node:
    def __init__(self, kid):
        self.kid = kid
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, current, kid):  # current is the root
        if not self.root:
            self.root = Node(kid)
        else:
            if kid.id < current.value:
                if current.left is None:
                    current.left = Node(kid)
                else:
                    self.add(current.left, kid)
            else:
                if current.right is None:
                    current.right = Node(kid)
                else:
                    self.add(current.right, kid)

    def visit(self, node):
        print(node.child.age)

    def preOrder(self, current):  # root,left,right
        self.visit(current)
        self.preOrder(current.left)
        self.preOrder(current.right)

    def inOrder(self, current):  # left, root, right
        self.inOrder(current.left)
        self.visit(current)
        self.inOrder(current.right)

    def postOrder(self, current):  # left, right, root
        self.postOrder(current.left)
        self.postOrder(current.right)
        self.visit(current)

    def prune(self, node):
        if node is None:
            return None

        node.left = self.prune(node.left)
        node.right = self.prune(node.right)

        if node.left is None and node.right is None:
            return None

        return node

    def removeById(self, node, kid_id):
        if not node:
            return None
        if kid_id < node.kid.id:
            node.left = self.removeById(node.left, kid_id)
        elif kid_id > node.kid.id:
            node.right = self.removeById(node.right, kid_id)
        else:

            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_node_right = self.findMin(node.right)
            node.kid = min_node_right

            node.right = self.removeById(node.right, min_node_right.id)

    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current