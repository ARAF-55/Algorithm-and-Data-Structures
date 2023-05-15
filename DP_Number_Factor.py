# Topdown approach

def numberFactorTD(n, tempDict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in tempDict:
            subP1 = numberFactorTD(n - 1, tempDict)
            subP2 = numberFactorTD(n - 3, tempDict)
            subP3 = numberFactorTD(n - 4, tempDict)
            tempDict[n] = subP1 + subP2 + subP3
        return tempDict[n]


print(numberFactorTD(5, {}))


# Bottom up approach

def numberFactorBU(n):
    tempArr = [1, 1, 1, 2]
    for i in range(4, n+1):
        tempArr.append(tempArr[i-1] + tempArr[i-3] + tempArr[i-4])
    return tempArr[n]


print(numberFactorBU(5))
