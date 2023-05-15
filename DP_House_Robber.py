# Topdown approach

def houseRobberTD(houses_set, currentIndex, tempDict):
    if currentIndex >= len(houses_set):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses_set[currentIndex] + houseRobberTD(houses_set, currentIndex + 2, tempDict)
            skipFirstHouse = houseRobberTD(houses_set, currentIndex + 1, tempDict)
            tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobberTD(houses, 0, {}))


# Bottom up approach

def houseRobberBU(houses_set, currentIndex):
    tempArr = [0] * (len(houses_set) + 2)
    for i in range(len(houses_set)-1, -1, -1):
        tempArr[i] = max(houses_set[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]


print(houseRobberBU(houses, 0))
