from collections import deque


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
            if kid.id < current.kid.id:
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
        if node is None:
            return None
        print(node.kid.id)

    def preOrder(self, current):  # root,left,right
        if current is None:
            return None
        self.visit(current)
        self.preOrder(current.left)
        self.preOrder(current.right)

    def inOrder(self, current):  # left, root, right
        if current is None:
            return None
        self.inOrder(current.left)
        self.visit(current)
        self.inOrder(current.right)

    def postOrder(self, current):  # left, right, root
        if current is None:
            return None
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

            node.right = self.removeById(node.right, min_node_right.kid.id)

    def findMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def find_node(self, node, id):

        if node is None or node.kid.id == id:
            return node
        elif id < node.kid.id:
            return self.find_node(node.left, id)
        else:
            return self.find_node(node.right, id)

    def has_children(self, id):

        node = self.find_node(self.root, id)
        if node is None:
            return f"El niño con el {id} no existe en el árbol."

        if node.left is not None or node.right is not None:
            return f"El nodo con el id {id} tiene hijos."
        else:
            return f"El nodo con id {id} no tiene hijos."

    def calculate_height(self, node):
        if not node:
            return 0
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        return max(left_height, right_height) + 1

    def count_nodes(self, node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def isComplete(self):
        if not self.root:
            return True
        height = self.calculate_height(self.root)

        num_nodes = self.count_nodes(self.root)

        expected_nodes = (2 ** height) - 1

        return num_nodes == expected_nodes

    def level_by_level_printing(self):
        if not self.root:
            return

        q1 = deque()
        q2 = deque()

        q1.append(self.root)

        while q1 or q2:

            while q1:
                node = q1.popleft()
                print(node.kid.id, end=" ")

                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)

            print()

            while q2:
                node = q2.popleft()
                print(node.kid.id, end=" ")

                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)

            print()


if __name__ == '__main__':

    child1 = Child(5, "Alice", 10, "F")
    child2 = Child(3, "Bob", 8, "M")
    child3 = Child(7, "Charlie", 12, "M")
    child4 = Child(2, "Diana", 6, "F")
    child5 = Child(4, "Edward", 9, "M")
    child6 = Child(6, "Fiona", 11, "F")
    child7 = Child(8, "George", 13, "M")

    tree = BST()

    tree.add(tree.root, child1)
    tree.add(tree.root, child2)
    tree.add(tree.root, child3)
    tree.add(tree.root, child4)
    tree.add(tree.root, child5)
    tree.add(tree.root, child6)
    tree.add(tree.root, child7)

    print("El árbol es completo:", tree.isComplete())

    print("Árbol nivel por nivel:")
    tree.level_by_level_printing()

    print("\nEliminando el nodo con ID 3:")
    tree.removeById(tree.root, 3)
    tree.level_by_level_printing()

    print("\nBuscando el nodo con ID 7:")
    found_node = tree.find_node(tree.root, 7)
    if found_node:
        print(f"Encontrado: {found_node.kid.name} con edad {found_node.kid.age}")
    else:
        print("No encontrado")

    print("\n¿El nodo con ID 5 tiene hijos?")
    print(tree.has_children(5))

    print("\nRecorrido en pre-orden:")
    tree.preOrder(tree.root)

    print("\n\nRecorrido en in-orden:")
    tree.inOrder(tree.root)

    print("\n\nRecorrido en post-orden:")
    tree.postOrder(tree.root)

    print("\nPodando el árbol:")
    tree.prune(tree.root)
    tree.level_by_level_printing()







