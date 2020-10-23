class Queue:
    def __init__(self):
        self.entries = []
        self.size = 0

    def __repr__(self):
        return "<" + str(self.entries)[1:-1] + ">"

    def enqueue(self, data):
        self.entries.append(data)
        self.size += 1

    def dequeue(self):
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return temp

    def size(self):
        return self.size

    def get(self, index):
        return self.entries[index]

    def reverse(self):
        self.entries = self.entries[::-1]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(f"队列: {queue}")
    print(f"删除的队列元素: {queue.dequeue()}")
    print(f"删除后的队列: {queue}")
    print(f"队列的大小: {queue.size}")
    index = 1
    print(f"查找的队列元素位置: {index}\n查找的队列元素为: {queue.get(index)}")
    queue.reverse()
    print(f"倒序后的队列: {queue}")


class Node:
    def __init__(self, data: any, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'Node({self.data})'


class LinkQueue:
    def __init__(self):
        self.front = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        node = Node(item)
        if self.size == 0:
            self.front = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
        self.size -= 1

    def is_empty(self):
        return self.front is None

    def __repr__(self):
        temp = self.front
        str_repr = ""
        while temp:
            str_repr += f"{temp}-->"
            temp = temp.next
        return str_repr + "END"

q = LinkQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
