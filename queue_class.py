class Queue:
    def __init__(self):
        self.Qu = []
    def enqueue(self, a):
        self.Qu.append(a)
    def dequeue(self):
        if self.is_empty:
            return None
        else:
            return self.Qu.pop()
    def front(self):
        if self.is_empty:
            return None
        else:
            return self.Qu[0]
    def is_empty(self):
        return len(self.Qu) == 0
    def size(self):
        return len(self.Qu)
    
Queue1 = Queue
Queue1.enqueue(10)
Queue1.enqueue(20)
Queue1.enqueue(30)
print(Queue1.dequeue())
print(Queue1.size())
print(Queue1.front())