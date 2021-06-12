from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self, val):
        self.container.append(val)
    def peek(self):
        return self.container[-1]
    def pop(self):
        return self.container.pop()
    def isEmpty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def display(self):
        return self.container
S= Stack()
S.push(3)
S.push([4,3])
print(S.peek())
print(S.pop())
print(S.isEmpty())
print(S.size())
print(S.display())
print(S.container)
