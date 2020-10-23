# class Student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def study(self,name):
#           print("%s正在学习"&(name))
#
#     def relax(self,name):
#           print("%s正在休息"%(name))
#
# s1 = Student('李四',11,'男')
# s1.relax(s1.name)
#
#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)

class Linklist:
    def __init__(self):
        self.head = None
        self.data = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        else:
            self.head = new_node
        self.head = new_node

    def append(self,data):
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
          str_repr += f"{temp}-->"
          temp = temp.next
        return str_repr + "END"

ll = Linklist()
ll.insert_head(1)
ll.insert_head(6)
ll.insert_head(3)
ll.insert_head(4)
ll.append(5)
print(ll)
