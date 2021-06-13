from collections import deque
class queue:
    def __init__(self):
        self.buffer= deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def isEmpty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
Q= queue()
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.dequeue())
print(Q.size())
print(Q.isEmpty())
print(Q.buffer)
