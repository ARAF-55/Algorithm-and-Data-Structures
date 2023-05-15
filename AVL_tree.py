import Queue_Linked_List_wise as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode is None:
        return "The value wasn't found here"
    else:
        if rootNode.data < nodeValue:
            searchNode(rootNode.leftChild, nodeValue)
        elif rootNode.data > nodeValue:
            searchNode(rootNode.rightChild, nodeValue)
        else:
            return "The value is found, success"


def getHeight(rootNode):
    if rootNode is None:
        return 0
    else:
        return rootNode.height


def rightRotate(disbalanceNode):
    new_root = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    new_root.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))
    return new_root


def leftRotate(disbalanceNode):
    new_root = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    new_root.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))
    return new_root


def getBalance(rootNode):
    if rootNode is None:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if rootNode is None:
        return AVLNode(nodeValue)
    else:
        if nodeValue <= rootNode.data:
            rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
        else:
            rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue <= rootNode.leftChild.data:
        rootNode = rightRotate(rootNode)
    elif balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        rootNode = rightRotate(rootNode)
    elif balance < -1 and nodeValue > rootNode.rightChild.data:
        rootNode = leftRotate(rootNode)
    elif balance < -1 and nodeValue <= rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        rootNode = leftRotate(rootNode)
    return rootNode


def getMinvalueNode(rootNode):
    current = rootNode
    while current.leftChild:
        current = current.leftChild
    return current


def getMaxvalueNode(rootNode):
    current = rootNode
    while current.rightChild:
        current = current.rightChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    else:
        if nodeValue < rootNode.data:
            rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
        else:
            if rootNode.leftChild is None:
                rootNode = rootNode.rightChild
                if rootNode is None:
                    return rootNode
            elif rootNode.rightChild is None:
                rootNode = rootNode.leftChild
                if rootNode is None:
                    return rootNode
            else:
                # minimum_value_node = getMinvalueNode(rootNode.rightChild)
                maximum_value_node = getMaxvalueNode(rootNode.leftChild)
                rootNode.data = maximum_value_node.data
                rootNode.leftChild = deleteNode(rootNode.leftChild, maximum_value_node.data)
        rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
        balance = getBalance(rootNode)
        if balance > 1 and getBalance(rootNode.leftChild) >= 0:
            rootNode = rightRotate(rootNode)
        elif balance > 1 and getBalance(rootNode.leftChild) < 0:
            rootNode.leftChild = leftRotate(rootNode.leftChild)
            rootNode = rightRotate(rootNode)
        elif balance < -1 and getBalance(rootNode.rightChild) <= 0:
            rootNode = leftRotate(rootNode)
        elif balance < -1 and getBalance(rootNode.rightChild) > 0:
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            rootNode = leftRotate(rootNode)
    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"


newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 76)
newAVL = insertNode(newAVL, 42)
newAVL = insertNode(newAVL, 97)
newAVL = insertNode(newAVL, 512)
newAVL = insertNode(newAVL, 3)
newAVL = deleteNode(newAVL, 10)
newAVL = deleteNode(newAVL, 76)
newAVL = insertNode(newAVL, 2)
newAVL = deleteNode(newAVL, 42)
newAVL = deleteNode(newAVL, 512)






levelOrderTraversal(newAVL)









