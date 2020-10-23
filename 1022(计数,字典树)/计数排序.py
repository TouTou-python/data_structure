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
