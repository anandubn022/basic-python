class stack:
    def __init__(self):
        self.stk = []
    def push(self, a):
        self.stk.append(a)      
    def pop(self):
        if self.not_empty():
            self.stk.pop()  
    def size(self):
        return len(self.stk)
    def not_empty(self):
        return len(self.stk) != 0
    def display(self):
        print(self.stk)

stack_1 = stack()
stack_1.push(20)
stack_1.push(30)
stack_1.pop()
stack_1.display()
stack_1.peek()