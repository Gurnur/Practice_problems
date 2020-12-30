class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.getMin())))
        else:
            self.stack.append((x,x))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.push(-4)
minStack.push(-5)
print(minStack.getMin())
minStack.pop()
minStack.pop()
print(minStack.getMin())
