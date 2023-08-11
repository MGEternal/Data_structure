class node:
    def __init__(self,data,next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data)
    
class l_list:
    def __init__(self):
        self.head = None
    def append(self,data):
        p = node(data)
        if self.head == None:
            self.head = p
        else:
            t=self.head
            while t.next != None:
                t = t.next
            t.next = p
            
    def __str__(self):
        if not self.head:
            return "Empty LinkedList"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current))
            current = current.next
        return " -> ".join(elements)
    def insertAfter(self,data,after):
        current =self.head
        new_node = node(data)
        while current:
            if current.data == after :
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        
ll = l_list()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.append("E")
ll.append("F")
print(f'After insert after {ll}')
ll.insertAfter("X","C")
ll.insertAfter("Y","C")
ll.insertAfter("Z","C")



print(f'before insert after {ll}')