class Stack:
    def __init__(self):
        self.items = []
    def Push(self, item):
        self.items.append(item)
    def Pop(self):
        return self.items.pop()
    def IsEmpty(self):
        return len(self.items) == 0
    def Size(self):
        return len(self.items)
    
S = Stack()
S.Push("A")
S.Push("B")
S.Push("C")
S.Push("D")
S.Push("E")
S.Push("F")
for i in range(S.Size()):
    print(S.Pop())
