class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        value = [str(x) for x in self.list]
        value.reverse()
        return '\n'.join(value)

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element is successfully pushed"

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            value = self.list[len(self.list)-1]
            self.list.pop()
            return value

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None
        return "The list is successfully deleted"


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.peek())
print(customStack)

