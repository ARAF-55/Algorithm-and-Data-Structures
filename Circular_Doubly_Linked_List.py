class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            if temp.next == self.tail.next:
                break
            temp = temp.next

    def createCDLL(self, nodeValue):
        new_node = Node(nodeValue)
        new_node.next = new_node
        new_node.prev = new_node
        self.head = new_node
        self.tail = new_node

    def insertCDLL(self, value, location):
        if self.head is None:
            return "There ain't no linked list"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node

    def traversalCDLL(self):
        if self.head is None:
            return "There is no linked list"
        else:
            for x in self:
                print(x)

    def reverseTraversalCDLL(self):
        if self.head is None:
            return "There is no linked list"
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                if temp.prev == self.tail:
                    break
                temp = temp.prev

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no linked list"
        else:
            for x in self:
                if x == nodeValue:
                    return x
            return "The value ain't present"

    def deleteNode(self, location):
        if self.head is None:
            return "There is no linked list"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.tail.next = None
                    self.tail.prev = None
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                temp.next = temp.next.next
                temp.next.prev = temp

    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")


circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
print([node for node in circularDLL])
circularDLL.deleteCDLL()
print([node for node in circularDLL])




