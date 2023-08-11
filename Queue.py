class Queue:
    def __init__(self):
        self.items = []
    def enQueue(self, item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def IsEmpty(self):
        return len(self.items) == 0
    def Size(self):
        return len(self.items)
    
Q = Queue()
Q.enQueue("A")
Q.enQueue("B")
Q.enQueue("C")
Q.enQueue("D")
Q.enQueue("E")
Q.enQueue("F")
for i in range(Q.Size()):
    print(Q.deQueue())
