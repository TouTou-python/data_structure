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
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

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
            prew = self.get(index - 1)
            new_node.next = prew.next
            prew.next = new_node
        self.size += 1


    def delete(self, index):
        if index < 0 or index > self.size:
            raise IndexError()
        elif self.size == 0:
            raise IndexError()
        elif index == 0:
            delete_node = self.head
            self.head = delete_node.next
            delete_node.next =None

        elif index == self.size - 1:
            prev = self.get(index-1)
            delete_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            delete_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return delete_node

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


ll = LinkList()
ll.insert(0, 5)
ll.insert(0, 6)
ll.insert(0, 2)
ll.insert(0, 5)
ll.insert(0, 4)
ll.insert(4, 10)

print(ll)