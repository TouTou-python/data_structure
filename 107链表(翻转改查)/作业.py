# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "node({})".format(self.data)

#


def circle(n):
    slow = fast = n
    while fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:

            return True
    return False

#
#
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n3
# print(circle(n1))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
        # return "Node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None
        self.head = None
        self.size = 0

    def get(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp



    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError()
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index-1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError()
        elif index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            prev.next = prev.next.next



    def reverse(self):
        pre = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = pre
            pre = temp
            temp = next_node
        self.head = pre


    def __repr__(self):
        temp = self.head
        str_repr = ""
        while temp:
            str_repr += f"{temp}-->"
            temp = temp.next
        return str_repr + "END"

    def __getitem__(self, index):
        temp = self.head
        if temp is None:
            raise IndexError ()
        for i in range(1,index):
            if temp.next is None:
                raise IndexError()
            else:
                temp = temp.next
        return temp


    def get(self, index):
        return self.__getitem__(index)

    def __setitem__(self, index, data):
        temp = self.head
        if temp is None:
            raise IndexError("the linklist is empty")

        for i in range(1, index):
            if temp.next is None:
                raise IndexError("index out of range")
            else:
                temp = temp.next
        temp.data = data

    def set(self, index, data):
        return self.__setitem__(index)
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#         # return "Node({})".format(self.data)
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#         self.head = None
#         self.size = 0
#
#     def get(self, index):
#         new_node = Node(data)
#         if index < 0 or index > self.size:
#             raise IndexError()
#         elif index == 0:
#
#     def insert(self, index, data):
#
#     def delete(self, index):
#
#     def reverse(self):
#
#     def __repr__(self):
#
#     def __getitem__(self, index):
#
#     def get(self, index):
#
#     def __setitem__(self, index, data):
#
#     def set(self, index, data):













class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
        # return "Node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        temp  = self.head
        for i in range (index):
            temp = temp.next
        return temp

    def insert(self, index, data):
        now_node = Node(data)
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        if self.size == 0:
            self.head = now_node
            self.tail = now_node
        if index == 0:
            now_node.next = self.head
            self.head = now_node
        if index == self.size:
            self.tail.next = now_node
            self.tail = now_node
        else:
            prev = self.get(index - 1)
            now_node.next = prev.next
            prev.next = now_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("")
        if index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
        if index == self.size - 1:
            prev = self.get(index - 1)
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            prev.next = prev.next.next
        self.size -= 1










    def reverse(self):
        pre = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = pre
            pre = temp
            temp = next_node
        self.head = pre


    def __getitem__(self, index):
        temp = self.head
        if temp == None:
            raise IndexError()
        for i in range(1,index):
            if temp.next == None:
                raise IndexError()
            else:
                temp =temp.next
        return temp


    def get(self, index):
        return self.__getitem__(index)
    def __setitem__(self, index, data):
        temp = self.head
        if temp == None:
            raise IndexError()
        for i in range(1, index):
            if temp.next == None:
                raise IndexError()
            else:
                temp = temp.next
        temp.data = data

    def set(self, index, data):
         return self.__setitem__(index,data)