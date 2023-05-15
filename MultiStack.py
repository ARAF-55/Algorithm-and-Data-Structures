class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (self.numstacks * stacksize)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def IsEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def IsFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False

    def IndexOfTop(self, stacknum):
        offset = self.stacksize * stacknum
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.IsFull(stacknum):
            return "The stack is full"
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.IsEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.array[self.IndexOfTop(stacknum)]
            self.array[self.IndexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self, stacknum):
        if self.IsEmpty(stacknum):
            return "The stack is empty"
        else:
            return self.array[self.IndexOfTop(stacknum)]


stack = MultiStack(1)
