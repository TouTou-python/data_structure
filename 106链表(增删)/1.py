# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "Node({})".format(self.data)
#
# class Linklist:
#     def __init__(self,data = None):
#         self.head = None
#
#     def insert_head(self, data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         else:
#             self.head = new_node
#         self.head = new_node
#
#
#     def append(self, data):
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = Node(data)
#         else:
#             self.insert_head(data)
#
#
#
#     def insert(self, i, data):
#         if self.head is None or i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             pre = temp
#             j = 1
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             node = Node(data)
#             pre.next = node
#             node.next = temp
#
#
#     def delete_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#             temp.next = None
#         else:
#             print("空链表")
#
#
#
#     def delete_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None
#
#
#     def __repr__(self):
#         temp = self.head
#         str_repr = ""
#         while temp:
#             str_repr += f'{temp} --> '
#             temp = temp.next
#         return str_repr + "END"
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "Node({})".format(self.data)
#
#
# class Linklist:
#     def __init__(self):
#         self.head = None
#
#     def insert_head(self, data):
#         new_node = Node(data)
#         if self.head:
#             new_node.next = self.head
#         else:
#             self.head = new_node
#
#     def append(self, data):
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = Node(data)
#         else:
#             self.insert_head(data)
#
#     def insert(self, i, data):
#         if self.head is None or i == 1:
#             self.insert_head(data)
#         else:
#             temp = self.head
#             pre = temp
#             j = 1
#             while j < i:
#                 pre = temp
#                 temp = temp.next
#                 j += 1
#             node = Node(data)
#             pre.next = node
#             node.next = temp
#
#     def delete_head(self):
#         temp = self.head
#         if self.head:
#             self.head = self.head.next
#         temp.next = None
#
#     def delete_tail(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             else:
#                 while temp.next.next:
#                     temp = temp.next
#                 temp.next = None
#
#     def __repr__(self):

#         temp = self.head
#         str_repr = ""
#         while temp:
#             str_repr += f"{temp}-->"
#             temp = temp.next
#         return str_repr + "END"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class Linklist:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        else:
            self.head = new_node

    def append(self, data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            temp = self.head
            pre = temp
            j = 1
            while j < i:
                pre = temp
                temp = temp.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = temp

    def delete_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
        temp.next = None

    def delete_tail(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def __repr__(self):
        temp = self.head
        str_repr = ""
        while temp:
            str_repr += f"{temp}-->"
            temp = temp.next
        return str_repr + "END"