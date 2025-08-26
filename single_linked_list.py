class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    def display(self):
        if self.head == None:
            print("Empty List")
            return
        current = self.head
        while current.next:
            print(current.data, sep= "", end=" ")
            current = current.next
        print(current.data)
    def insert_front(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        previousfront = self.head
        self.head = newnode
        newnode.next = previousfront
    def insert_after(self, prev, data):
        current = self.head
        while current:
            if current.data == prev:
                newnode = Node(data)
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
        print(f"{prev} not found")
    def delete_front(self):
        if self.head!=None:
            self.head = self.head.next
    def delete_end(self):
        if self.head!= None:
            current = self.head
            prev = None
            while current.next!=None:
                prev = current
                current=current.next
            prev.next = None
    def delete_key(self, key):
        if self.head!=None:
            current = self.head
            prev = None
            while current.next!=None and current.data != key:
                prev = current
                current = current.next
            if current.data == key:
                prev.next = current.next

L1 = LinkedList()
L1.insert_end(10)
L1.insert_end(20)
L1.insert_end(30)
L1.insert_front(00)
L1.insert_after(20, 25)
L1.delete_front()
L1.delete_end()
L1.delete_key(20)
L1.display()