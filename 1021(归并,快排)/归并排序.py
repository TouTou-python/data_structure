

def mergeSort(iList):
    if len(iList) <= 1:
        return iList
    middle = len(iList) // 2
    left, right = iList[0:middle], iList[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    while left:
        mList.append(left.pop(0))
    while right:
        mList.append(right.pop(0))

    return mList

print(mergeSort([12,45,34,56,67,23,34,45]))



# 双指针
def merge1(left,right):
    left_len = len(left)
    right_len = len(right)
    mList =[]
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            mList.append(left[i])
            i += 1
        else:
            mList.append(right[j])
            j += 1

    mList.extend(left[i:])
    mList.extend(left[j:])
    return mList













class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class Linklist:
    def __init__(self):
        self.head = None