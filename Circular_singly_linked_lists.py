class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next
            if temp == self.tail.next:
                break

    def createCSLL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            elif location == 1:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                next_node = temp.next
                temp.next = new_node
                new_node.next = next_node
            return "The node has been successfully inserted"

    def traversalCSLL(self):
        if self.head is None:
            print("There is no element for traversal")
        for x in self:
            print(x)

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the CSLL"
        else:
            temp = self.head
            while temp:
                if temp.value == nodeValue:
                    return temp.value
                temp = temp.next
                if temp == self.tail.next:
                    return "The node doesn't exist in the CSLL"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                temp = self.head
                while temp:
                    if temp.next == self.tail:
                        break
                    temp = temp.next
                temp.next = self.head
                self.tail = temp
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                next_node = temp.next
                temp.next = next_node.next

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(1, 1)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)

circularSLL.traversalCSLL()
