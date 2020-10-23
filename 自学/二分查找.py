numbers = [1, 2, 4, 5, 6, 7, 8, 9, 13, 16, 17, 34, 45]
head, tail = 0, len(numbers)
search = int(input("enter a number to search:"))

while tail > head:
    mid = (head + tail) // 2
    if search < numbers[mid]:
        tail = mid
    elif search > numbers[mid]:
        head = mid + 1
    elif search == numbers[mid]:
        result = mid
        break
else:
    if search == numbers[head]:
        result = head
    else:
        result = -1
print(result)
