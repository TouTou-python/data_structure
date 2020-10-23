
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class Linklist:
    def __init__(self, data=None):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        else:
            self.head = new_node
        self.head = new_node

    def append(self, data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def __repr__(self):
        temp = self.head
        str_repr = ""
        while temp:
            str_repr += f"{temp} -->"
            temp = temp.next
        return str_repr + "END"

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

    def linklist(self, object: List):
        new_node = Node(object[0])
        self.head = new_node
        curr = self.head
        for i in object[1:]:
            curr.next = Node(i)
            curr = curr.next

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

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    def __getitem__(self, index):
        temp = self.head
        if temp is None:
            raise IndexError("the linklist is empty")

        for i in range(1, index):
            if temp.next is None:
                raise IndexError("index out of range")
            else:
                temp = temp.next
        return temp

    def get(self,index):
        return self.__getitem__(index)

    def __setitem__(self, index,data):
        temp = self.head
        if temp is None:
            raise IndexError("the linklist is empty")

        for i in range(1, index):
            if temp.next is None:
                raise IndexError("index out of range")
            else:
                temp = temp.next
        temp.data = data

    def set(self,index,data):
        return self.__setitem__(index,data)


ll = Linklist()
ll.insert_head(1)
ll.insert_head(6)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
ll.insert(3, 10)
ll.delete_head()
ll.delete_tail()
ll.reverse()
print(ll.get(3))
ll.set(2,100)
# ll.linklist(["a", "b", 3, 4, 5])
print(ll)
