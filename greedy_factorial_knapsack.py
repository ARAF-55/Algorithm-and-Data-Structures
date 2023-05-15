class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = self.value / self.weight


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        if usedCapacity == capacity:
            break
    print("Total value obtained: " + str(totalValue))
