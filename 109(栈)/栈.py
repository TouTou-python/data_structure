# 列表实现栈
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def push(self,data):
#         self.stack.append(data)
#         self.size += 1
#
#     def pop(self):
#         if self.stack:
#             temp = self.stack.pop()
#             self.size -= 1
#             return temp
#         else:
#             raise IndexError()
#
#     def peek(self):
#         return self.stack[-1]
#
#     def is_empity(self):
#         return not bool(self.stack)
#
#     def sizeof(self):
#         return self.size
#
# if __name__ == '__main__':
#     ll = Stack( )


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class Linkstack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        del_node = self.top
        self.top = del_node.next
        del_node.next = None
        self.size -= 1
        return del_node

    def is_empty(self):
        return self.top is None
