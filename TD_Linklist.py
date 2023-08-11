class priNode:
    def __init__(self,pri_data,next=None):
        self.data = {'keys': pri_data, 'values': []}
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data['keys'])
    
class secNode:
    
    def __init__(self, pri_node, sec_data, next=None):
        pri_node
        self.pri_node = pri_node
        self.data = sec_data
        if next is None:
            self.next = None
        else:
            self.next = next
    def __str__(self):
        return str(self.data)
    
class TDLinkedList:
    def __init__(self):
        self.head = None
    def Append_primary(self,pri_data):
        p = priNode(pri_data)
        if self.head == None:
            self.head = p
        else:
            t=self.head
            while t.next != None:
                t = t.next
            t.next = p
            
    def Append_secondary(self,pri_data,sec_data):
        p = secNode(pri_data,sec_data)
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
            primary_key = str(current)
            secondary_values = ",".join(current.data['values'])
            element = f"{primary_key} : {secondary_values}"
            elements.append(element)
            current = current.next
        return "\n".join(elements)
    def find_pri_node(self,pri_data):
        current = self.head
        while current:
            if current.data['keys']==pri_data:
                return print(f"{current.data['keys']}")
            else:
                return print(f"not found this pri_node")
ll = TDLinkedList()
ll.Append_primary("A")
ll.Append_primary("B")
ll.Append_primary("C")
ll.find_pri_node("A")
ll.find_pri_node("X")






