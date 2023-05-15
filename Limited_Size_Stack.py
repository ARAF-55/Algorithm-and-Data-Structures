class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        values.reverse()
        return '\n'.join(values)

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, item):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(item)

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)