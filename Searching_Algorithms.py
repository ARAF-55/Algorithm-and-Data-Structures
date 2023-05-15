def linearSearch(customList, value):
    for i in range(len(customList)):
        if customList[i] == value:
            return i
    return -1


def binarySearch(customList, value):
    start = 0
    end = len(customList) - 1
    while 0 <= start <= end:
        mid = (start + end) // 2
        if customList[mid] == value:
            return mid
        elif customList[mid] < value:
            start = mid + 1
        elif customList[mid] > value:
            end = mid - 1
    return -1


print(binarySearch([8, 9, 12, 15, 17, 19, 20, 21, 28], 12))
