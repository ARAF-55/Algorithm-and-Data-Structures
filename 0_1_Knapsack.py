class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zoKnapsack(items_set, capacity, currentIndex):
    if currentIndex < 0 or currentIndex >= len(items_set):
        return 0
    elif items_set[currentIndex].weight <= capacity:
        profit1 = items_set[currentIndex].profit + zoKnapsack(items_set, capacity - items_set[currentIndex].weight,
                                                              currentIndex + 1)
        profit2 = zoKnapsack(items_set, capacity, currentIndex + 1)
        return max(profit1, profit2)
    else:
        return zoKnapsack(items_set, capacity, currentIndex + 1)


mango = Item(31, 8)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))
