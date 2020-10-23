from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=1)
        # 结点:(结点的左孩子,结点的右孩子)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        return self.root is None

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
                new_node.parent = parent_node

    def pre_order(self, node):
        self.root = node
        print(node)
        self.pre_order(node.left)
        self.pre_order(node.right)
        return

    def in_order(self, node):
        self.root = node
        self.pre_order(node.left)
        print(node)
        self.pre_order(node.right)
        return

    def pre_order_stcak(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                print(node.value)
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                node = node.right














