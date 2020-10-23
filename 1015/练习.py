# from pprint import pformat
#
#
# class Node:
#     def __init__(self, data, parent):
#         self.left = None
#         self.right = None
#         self.parent = parent
#         self.data = data
#
#     def __repr__(self):
#         if self.left is None and self.right is None:
#             return str(self.data)
#         return pformat({"%s" % (self.data): (self.left, self.right)})
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def __str__(self):
#         return str(self.root)
#
#     def is_empty(self):
#         if self.root:
#             return False
#         return True
#
#     def __insert(self, data):
#         new_node = Node(data, None)
#         if self.is_empty():
#             self.root = new_node
#         else:
#             parent_node = self.root
#             while True:
#                 if data < parent_node.data:
#                     if parent_node.left is None:
#                         parent_node.left = new_node
#                         break
#                     else:
#                         parent_node = parent_node.left
#                 else:
#                     if parent_node.right is None:
#                         parent_node.right = new_node
#                         break
#                     else:
#                         parent_node = parent_node.right
#             new_node.parent = parent_node
#
#     def is_right(self, node):
#         return node == node.parent.right
#
#     def insert(self, *values):
#         for value in values:
#             self.__insert(value)
#         return self
#
#     def search(self, data):
#         if self.is_empty():
#             raise IndexError()
#         else:
#             node = self.root
#             while node and node.data != data:
#                 if data < node.data:
#                     node = node.left
#                 if data > node.data:
#                     node = node.right
#             print(node)
#             return node
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
#                 tmp_node = self.get_max(node.left)
#                 self.remove(tmp_node.data)
#                 node.data = tmp_node.data
#
#
#     def get_max(self, node=None):
#         if node is None:
#             node = self.root
#         if not self.is_empty():
#             while node.right is not None:
#                 node = node.right
#         return node
#
#
# if __name__ == '__main__':
#     bst = BST().insert(8, 3, 6, 1)
#     print(bst)
#     bst.remove(1)
#     print(bst)
# import time
# def f(n):
#     if n <= 2:
#         return 1
#     else:
#         return f(n - 1) + f(n - 2)
#
# start = time.time()
# print(f(40))
# end =time.time()
# dur = end - start
# print(dur)