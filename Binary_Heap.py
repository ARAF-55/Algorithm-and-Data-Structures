class Heap:
    def __init__(self, size):
        self.max_size = size + 1
        self.customList = [None] * (size + 1)
        self.heapSize = 0


def peekofHeap(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.customList[1]


def sizeofHeap(rootNode):
    if rootNode is None:
        return
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    else:
        if heapType == 'Min':
            if rootNode.customList[index] < rootNode.customList[parentIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[parentIndex]
                rootNode.customList[parentIndex] = temp
                heapifyTreeInsert(rootNode, parentIndex, heapType)
            else:
                return
        elif heapType == 'Max':
            if rootNode.customList[index] > rootNode.customList[parentIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[parentIndex]
                rootNode.customList[parentIndex] = temp
                heapifyTreeInsert(rootNode, parentIndex, heapType)
            else:
                return


def inserNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.max_size:
        return "The heap is full"
    else:
        rootNode.customList[rootNode.heapSize + 1] = nodeValue
        rootNode.heapSize += 1
        if heapType == 'Min':
            heapifyTreeInsert(rootNode, rootNode.heapSize, 'Min')
        elif heapType == 'Max':
            heapifyTreeInsert(rootNode, rootNode.heapSize, 'Max')


def heapifyTreeExtract(rootNode, index, heapType):
    leftChild_index = index * 2
    rightChild_index = index * 2 + 1
    swapchild = 0
    if leftChild_index > rootNode.heapSize:
        return
    elif leftChild_index == rootNode.heapSize:
        if heapType == 'Min':
            if rootNode.customList[leftChild_index] < rootNode.customlist[index]:
                temp = rootNode.customList[leftChild_index]
                rootNode.customList[leftChild_index] = rootNode.customlist[index]
                rootNode.customlist[index] = temp
                return
        elif heapType == 'Max':
            if rootNode.customList[leftChild_index] > rootNode.customlist[index]:
                temp = rootNode.customList[leftChild_index]
                rootNode.customList[leftChild_index] = rootNode.customlist[index]
                rootNode.customlist[index] = temp
                return
    else:
        if heapType == 'Min':
            if rootNode.customList[leftChild_index] < rootNode.customList[rightChild_index]:
                swapchild = leftChild_index
            else:
                swapchild = rightChild_index
            if rootNode.customList[index] > rootNode.customList[swapchild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp
                heapifyTreeExtract(rootNode, swapchild, heapType)
        elif heapType == 'Max':
            if rootNode.customList[leftChild_index] < rootNode.customList[rightChild_index]:
                swapchild = rightChild_index
            else:
                swapchild = leftChild_index
            if rootNode.customList[index] < rootNode.customList[swapchild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp
                heapifyTreeExtract(rootNode, swapchild, heapType)


def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return "The heap is empty"
    else:
        value = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return value


def deleteEntireBP(rootNode):
    rootNode.customList = None


newHeap = Heap(31)
inserNode(newHeap, 4, "Min")
inserNode(newHeap, 77, "Min")
inserNode(newHeap, 2, "Min")
inserNode(newHeap, 1, "Min")
inserNode(newHeap, 32, "Min")
inserNode(newHeap, 22, "Min")
inserNode(newHeap, 8, "Min")
inserNode(newHeap, 7, "Min")
inserNode(newHeap, 45, "Min")
inserNode(newHeap, 65, "Min")
val = extractNode(newHeap, "Min")
val = extractNode(newHeap, "Min")
print(val)

