from randList import randList


def insertSort(List):
    if len(List) <= 1:
        return List
    for right in range(1, len(List)):
        target = List[right]
        for left in range(0, right):
            if List[left] > target:
                List[left + 1:right + 1] = List[left:right]
                List[left] = target
                break
        print(List)


insertSort(randList.randList(10))


# 链表的插入排序
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)

def insertionSortList(head):
    dummy = ListNode(0)
    pre = dummy
    cur = head
    while cur is not None:
        temp = cur.next
        while pre.next is not None and pre.next.data < cur.data:
            pre = pre.next

        cur.next = pre.next
        pre.next = cur

        cur = temp
        pre = dummy

    return dummy.next



