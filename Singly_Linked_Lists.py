class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def insertSLL(self, value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                self.tail.next = new_node
                new_node.next = None
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

    def traverse(self):
        if self.head is None:
            print("The singly linked list doesn't exist")
        else:
            for x in self:
                print(x)

    def searchSLL(self, value):
        if self.head is None:
            return "the singly linked list is non-existent"
        else:
            temp = self.head
            while temp:
                if temp.value == value:
                    return temp.value
                temp = temp.next
            return "The node doesn't exist in the linked list"

    def deleteNode(self, location):
        if self.head is None:
            return "The singly linked list doesn't exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp = self.head
                    while temp:
                        if temp.next == self.tail:
                            break
                        temp = temp.next
                    temp.next = None
                    self.tail = temp
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                next_node = temp.next
                temp.next = next_node.next

    def deleteEntireSll(self):
        if self.head is None:
            print("The linked list doesn't exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(0, 4)


print([node for node in singlyLinkedList])
singlyLinkedList.deleteEntireSll()
print([node for node in singlyLinkedList])




