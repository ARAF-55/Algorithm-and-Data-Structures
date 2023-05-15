class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def isEmpty(self):
        return self.list == []

    def enqueue(self, value):
        self.list.append(value)
        return "The element is inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The quque is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
print(customQueue)
customQueue.delete()
