# from pprint import pformat
#
#
# class Node:
#     def __init__(self, value, parent):
#         self.value = value  # self.data =
#         self.parent = parent
#         self.left = None
#         self.right = None
#
#     def __repr__(self):
#         if self.left is None and self.right is None:
#             return str(self.value)
#         return pformat({"%s" % (self.value): ( self.left, self.right)}, indent=1)
#
#
# class BinarySearchTree:
#     def __init__(self, root=None):
#         self.root = root
#
#     def __str__(self):
#         return str(self.root)
#
#     def is_empty(self):
#         if self.root is None:
#             return True
#         return False
#
#     def __insert(self, value):
#         new_node = Node(value, None)
#         if self.is_empty():
#             self.root = new_node
#         else:
#             parent_node = self.root
#             while True:
#                 if value < parent_node.value:
#                     if parent_node.left:
#                         parent_node = parent_node.left
#                     else:
#                         parent_node.left = new_node
#                         break
#                 elif value >= parent_node.value:
#                     if parent_node.right:
#                         parent_node = parent_node.right
#                     else:
#                         parent_node.right = new_node
#                         break
#             new_node.parent = parent_node
#
#     def insert(self, *values):
#         for value in values:
#             self.__insert(value)
#         return self
#
#     def search(self, value):
#         if self.is_empty():
#             raise IndexError("空")
#         else:
#             node = self.root
#             while node and node.value != value:
#                 if value < node.value:
#                     node = node.left
#                 else:
#                     node = node.right
#             print(node)
#             return node
#
#     def is_right(self, node):
#         return node == node.parent.right
#
#     def __reassign_nodes(self, node, new_children):
#         if new_children is not None:
#             new_children.parent = node.parent
#         if node.parent is not None:
#             if self.is_right(node):
#                 node.parent.right = new_children
#             else:
#                 node.parent.left = new_children
#         else:
#             self.root = new_children
#
#     def remove(self, data):
#         node = self.search(data)
#         if node is not None:
#             if node.left is None and node.right is None:
#                 self.__reassign_nodes(node, None)
#             elif node.left is None:
#                 self.__reassign_nodes(node, node.right)
#             elif node.right is None:
#                 self.__reassign_nodes(node, node.left)
#             else:
#                 temp_node = self.get_max(node.left)
#                 self.remove(temp_node.data)
#                 node.data = temp_node.data
#
#     def get_max(self, node=None):
#         if node is None:
#             node = self.root
#         if not self.is_empty():
#             while node.right is not None:
#                 node = node.right
#         return node
#
#     def preOrder(self, node):
#         if node is None:
#             return
#         print(node)
#         self.preOrder(node.left)
#         self.preOrder(node.right)
#
#     def inOrder(self, node):
#         if node is None:
#             return
#         self.preOrder(node.left)
#         print(node)
#         self.preOrder(node.right)
#
#
# if __name__ == '__main__':
#     bst = BinarySearchTree().insert(8, 3, 6, 1)
#     print(bst)
#     # bst.remove(1)
#     # print(bst)

# def f(n):
#     count = 0
#     while n != 0:
#       n = n & (n-1)
#       count += 1
#     return count
#
# print(f(15))

# def f(n):
#     res = 0
#     for i in n:
#         res = res ^ i
#     return res
#
# print(f([4,5,3,4,5]))

#


def f(a, b):
    for i in range(min(a, b) // 2, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(f(56, 72))


def f1(a, b):
    sm = min(a, b)
    big = max(a, b)
    if big % sm == 0:
        return sm
    return f1(sm, big % sm)


def f2(a, b):
    if b - a == 0:
        return b
    sm = min(a, b)
    big = max(a, b)
    return f2(big - sm, sm)


print(f2(56, 72))


# def f(n):
#     if n == 1:
#         return n
#     return f(n-1) * n
# 0
# print(f(5))
#
# def f(n):
#     if n <= 2:
#         return n
#     else:
#         return f(n-1)+f(n-2)
#
# print(f(5))
