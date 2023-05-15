class BinaryTree:
    def __init__(self, size):
        self.max_size = size
        self.customList = [None] * size
        self.lastUsedIndex = 0

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.max_size:
            return "The Binary tree is full"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal(2 * index + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2 * index)
        print(self.customList[index])
        self.inOrderTraversal(2 * index + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2 * index)
        self.postOrderTraversal(2 * index + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "The binary tree is empty"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Successfully deleted the node"

    def deleteBT(self):
        self.customList = None
        return "It is completely deleted"


newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.levelOrderTraversal(1)
