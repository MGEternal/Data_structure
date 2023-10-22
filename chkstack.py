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
    def peek(self):
        return self.items[len(self.items)-1]
    

S = Stack()
list = "()()()("
           
            

for i in list :
    if i == "(":
        S.Push(i)
    elif i == ")":
        if S.IsEmpty():
            print("False")
        elif S.peek() == '(' :
            S.Pop()
if S.IsEmpty():
    print("True")
else:
    print("False")
    


