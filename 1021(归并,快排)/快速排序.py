def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(iList, start, end):
    pivot = iList[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and iList[p] < pivot:
            p += 1
        while p <= q and iList[q] >= pivot:
            q -= 1
        if p < q:
            swap(iList, p, q)
    swap(iList, start, q)
    return q


def quickSort(iList, start, end):
    if start >= end:
        return
    mid = partition(iList, start, end)
    quickSort(iList, start, mid - 1)
    quickSort(iList, mid + 1, end)


from randList import randList

l = randList.randList(10)
print(l)
quickSort(l,0,len(l)-1)
print(l)


# 单指针遍历

from randList import randList


def quickSort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quickSort(array, l, q - 1)
        quickSort(array, q + 1, r)


def partition(array, l, r):
    pivot = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            print(array)
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

def partition1(array,start,end):
    pivot = array[start]
    mark = start
    for i in range(start+1,end):
        if array[i] < pivot:
            mark += 1
            array[mark],array[i] = array[i],array[mark]
        array[start] = array[mark]
        array[mark] = pivot

if __name__ == '__main__':
    iList = randList.randList(20)
    print("原列表为：%s" % iList)
    quickSort(iList, 0, len(iList) - 1)
    print("新列表为：%s" % iList)
