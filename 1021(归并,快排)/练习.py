# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "node({})".format(self.data)
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#
#     def reverse(self):
#         pre = None
#         temp =self.head
#         while temp:
#             next_node = temp.next
#             temp.next = pre
#             pre = temp
#             temp = next_node
#         self.head = pre
#
#
# def reverse(s):
#     head = 0
#     tail = len(s)-1
#     while head < tail:
#         s[head],s[tail] = s[tail],s[head]
#         head += 1
#         tail -= 1
#     return s
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def f(self, node):
        dummy = Node(0)
        self.head = node
        pre = node
        dummy.next = pre
        cur = pre.next
        next_node = cur.next
        while pre.next and pre.next.next:
            cur.next = pre
            cur = next_node.next
            pre.next = cur
            pre = next_node
            next_node = cur.next
        return dummy.next

    def __repr__(self):
        temp = self.head
        str_repr = ""
        while temp:
            str_repr += f"{temp} -->"
            temp = temp.next
        return str_repr + "END"


ll = LinkList()

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll.f(n0)
