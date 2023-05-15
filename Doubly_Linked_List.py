class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next

    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def insertNode(self, value, location):
        if self.head is None:
            return "There is no linked list to insert"
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == 1:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                next_node = temp.next
                temp.next = node
                node.prev = temp
                node.next = next_node
                next_node.prev = node

    def traverseDLL(self):
        if self.head is None:
            return "There ain't no fucking linked list here"
        else:
            for x in self:
                print(x)

    def reverseTraversalDLL(self):
        if self.head is None:
            return "There ain't no fucking linked list here"
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                temp = temp.prev

    def searchDLL(self, value):
        if self.head is None:
            return "There ain't no fucking linked list here"
        else:
            temp = self.head
            while temp:
                if temp.value == value:
                    return temp.value
                else:
                    temp = temp.next
            return "The value ain't present in the linked list"

    def deleteNode(self, location):
        if self.head is None:
            return "The linked list is not present"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                temp.next = temp.next.next
                temp.next.prev = temp

    def deleteDLL(self):
        if self.head is None:
            return "There is no"
        else:
            self.head.next = None
            self.tail.prev = None
            self.head = None
            self.tail = None


doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0, 0)
doubyLL.insertNode(2, 1)
doubyLL.insertNode(6, 2)
print([node for node in doubyLL])
doubyLL.deleteDLL()
print([node for node in doubyLL])
