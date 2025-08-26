stack = []

def is_empty():
    return len(stack) == 0
def push(a):
    stack.append(a)
def pop():
    if not is_empty():
        return stack.pop()
    else:
        return None
    
push(20)
push(30)
pop()
print(stack)