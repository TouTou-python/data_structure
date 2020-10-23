# from randList import randList
#
#
# def swap(ilist, a, b):
#     ilist[a], ilist[b] = ilist[b], ilist[a]
#
# `
# def partition(iList, start, end):
#     pivot = iList[start]
#     p = start + 1
#     q = end
#     while p <= q:
#         while p <= q and iList[p] < pivot:
#             p += 1
#         while p <= q and iList[q] >= pivot:
#             q -= 1
#         if p < q:
#             swap(iList, p, q)
#     swap(iList, start, q)
#     return q
#
#
# def partition1(array, start, end):
#     pivot = array[start]
#     mark = start
#     for i in range(start + 1, end):
#         if array[i] < pivot:
#             mark += 1
#             array[mark], array[i] = array[i], array[mark]
#         array[start] = array[mark]
#         array[mark] = pivot
#
#
# def quickSort(iList, start, end):
#     if start >= end:
#         return
#     mid = partition(iList, start, end)
#     quickSort(iList, start, mid - 1)
#     quickSort(iList, mid + 1, end)
#
#
# if __name__ == '__main__':
#     iList = randList.randList(20)
#     print("原列表为：%s" % iList)
#     quickSort(iList, 0, len(iList) - 1)
#     print("新列表为：%s" % iList)
#
#
# class TrieNode:
#     def __init__(self):
#         self.data = {}
#         self.is_word = False
#
#     def __repr__(self):
#         return str(self.data)
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self,word):
#         node = self.root
#         for char in word:
#             child = node.data.get(char)
#             if child is None:
#                 node.data[char] = TrieNode()
#             node = node.data[char]
#         node.is_word = True


def countSort(ilist):
    result = []
    mlist = [0] * (max(ilist)+1)

    for i in ilist:
        mlist[i] += 1
    for k in range(len(mlist)):
        while mlist[k] != 0:
            result.append(k)
            mlist[k] -= 1
    return result



print(countSort([9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]))


