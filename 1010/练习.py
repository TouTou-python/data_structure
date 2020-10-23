# class stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def push(self, data):
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
#     def is_empty(self):
#         return not bool(self.stack)
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"Node({self.data})"
#
#
# class Linkstack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def push(self, data):
#         new_node = Node(data)
#         if self.top:
#             new_node.next = self.top
#             self.top = new_node
#         else:
#             self.top = new_node
#
#     def pop(self):
#         if self.top:
#             temp = self.top
#             self.top = temp.next
#             temp.next = None
#             self.size -= 1
#             return temp
#
#         else:
#             raise IndexError()
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return f"Node({self.val})"

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = cur = ListNode(0)  # 一般是真实的头结点head/ /虚拟节点dummy, 是留守，最后用于返回的； cur是跟着走的
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next  # cur.next, l1 = l1, l1.next 顺序很重要，暂时还是不要这么写
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2  # 三元组的写法
        return dummy.next




ll = Solution()
l1 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
l1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
l2 = ListNode(0)
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)
l2.next = p1
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6

a = ll.mergeTwoLists(l1,l2)
print(a)


