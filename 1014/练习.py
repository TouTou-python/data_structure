# def twoSum(nums, target):
#     dict = {}
#     for i in range(len(nums)):
#         m = nums[i]
#         if target - m in dict:
#             return target - m, i
#         dict[m] = i
#
#
# def two_sum(nums, target):
#     nums.sort()
#     slow = 0
#     fast = len(nums) - 1
#     while slow < fast:
#         if nums[slow] + nums[fast] < target:
#             slow += 1
#         if nums[slow] + nums[fast] > target:
#             fast -= 1
#         else:
#             return slow, fast
#     return slow, fast


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.right = None
#         self.left = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
# from pprint import pformat
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def add(self, data):
#         node = Node(data)
#         if self.root:
#             self.root = node
#         else:
#             temp = [self.root]
#             while True:
#                 pop_node = temp.pop(0)
#                 if pop_node.left is None:
#                     pop_node.left = node
#                     break
#                 if pop_node.right is None:
#                     pop_node.right = node
#                     break
#                 else:
#                     temp.append(pop_node.left)
#                     temp.append(pop_node.right)
#
#     def get_parent(self, data):
#         if self.root.data == data:
#             return None
#         temp = [self.root]
#         while temp:
#             pop_node = temp.pop(0)
#             if pop_node.left.data == data:
#                 return pop_node
#             if pop_node.right.data == data:
#                 return pop_node
#             if pop_node.left is None:
#                 temp.append(pop_node.left)
#             if pop_node.right is None:
#                 temp.append(pop_node.right)
#         return None

from pprint import pformat
class Node:
    def __init__(self, data, parent):
        self.right = None
        self.left = None
        self.data = data
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s"%(self.data):(self.left,self.right)},indent=1)

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self,data):
        new_node = Node(data,None)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left:
                        parent_node = parent_node.left

                    else:
                        parent_node.left = new_node
                        break
                else:
                    if data > parent_node.data:
                        if parent_node.right:
                            parent_node = parent_node.right

                        else:
                            parent_node.right = new_node
                            break
            new_node.parent = new_node

    def insert(self,*values):
        for value in values:
            self.insert(value)
        return self