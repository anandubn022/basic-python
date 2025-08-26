queu = []

def enqueu(a):
    queu.append(a)

def dequeu():
    if is_empty():
        return None
    else:
        return queu.pop(0)

def front():
    if is_empty():
        return None
    else:
        return queu[0]

def is_empty():
    return len(queu) == 0

def size():
    return len(queu)


enqueu(10)
enqueu(20)
enqueu(30)
print(dequeu())  
print(front())   
print(size())