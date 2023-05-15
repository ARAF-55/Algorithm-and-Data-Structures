def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        steal_first_house = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skip_first_house = houseRobber(houses, currentIndex + 1)
        return max(steal_first_house, skip_first_house)


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0))
