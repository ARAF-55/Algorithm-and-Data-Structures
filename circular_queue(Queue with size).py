class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * self.max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.start == -1 and self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.start == 0 and self.top + 1 == self.max_size:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "The circular queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
                self.items[self.top] = value
            else:
                self.top += 1
                self.items[self.top] = value
                if self.start == -1:
                    self.start += 1

    def dequeue(self):
        if self.isEmpty():
            return "The circular queue is empty"
        else:
            first_element = self.items[self.start]
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.items[self.start] = None
                self.start = 0
            else:
                self.items[self.start] = None
                self.start += 1
            return first_element

    def peek(self):
        if self.isEmpty():
            return "THe queue is empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1


customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)