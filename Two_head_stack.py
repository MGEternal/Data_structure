class Stack:
    def __init__(self):
        self.items = []
    def Push_left(self, item):
        self.items.append(item)
    def Pop_left(self):
        return self.items.pop()
    def IsEmpty(self):
        return len(self.items) == 0
    def Size(self):
        return len(self.items)
    def Push_right(self, item):
        self.items.insert(0, item)
    def Pop_right(self):
        return self.items.pop(0)
S = Stack()
S.Push_left("A")
S.Push_left("B")
S.Push_left("C")
S.Push_left("D")
print("Push_left || Pop_right")
for i in range(S.Size()):
    print(S.Pop_right(), end=" ")
