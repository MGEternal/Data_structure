class priNode:
    def __init__(self, pri_data, next=None):
        self.data = {'keys': pri_data, 'values': []}
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data['keys'])
    
class secNode:
    def __init__(self, pri_node, sec_data, next=None):
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
    
    def Append_primary(self, pri_data):
        p = priNode(pri_data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
    def Delete_primary(self, pri_data):
        current = self.head
        prev = None
        
        while current:
            if current.data['keys'] == pri_data:
                if prev is None:  # If deleting the head node
                    self.head = current.next
                else:
                    prev.next = current.next
                del current
                return
            prev = current
            current = current.next
        
        print(f"No primary node with data: {pri_data}")
        
    def Delete_secondary(self, pri_data, sec_data):
        pri_node = self.find_pri_node(pri_data)
        if pri_node is not None:
            sec_nodes = pri_node.data['values']
            for sec_node in sec_nodes:
                if sec_node.data == sec_data:
                    sec_nodes.remove(sec_node)
                    return
            print(f"No secondary node with data: {sec_data} for primary node: {pri_data}")
        else:
            print(f"No primary node with data: {pri_data}")
    def Append_secondary(self, pri_data, sec_data):
        pri_node = self.find_pri_node(pri_data)
        if pri_node is not None:
            p = secNode(pri_node, sec_data)
            pri_node.data['values'].append(p)
        else:
            print(f"No primary node with data: {pri_data}")
            
    def find_pri_node(self, pri_data):
        current = self.head
        while current:
            if current.data['keys'] == pri_data:
                return current
            current = current.next
        return None
    
    def __str__(self):
        if not self.head:
            return "Empty LinkedList"
        
        elements = []
        current = self.head
        while current:
            primary_key = str(current)
            secondary_values = ",".join(str(sec) for sec in current.data['values'])
            element = f"{primary_key} : {secondary_values}"
            elements.append(element)
            current = current.next
        return "\n".join(elements)

ll = TDLinkedList()
ll.Append_primary("A")
ll.Append_primary("B")
ll.Append_primary("C")
ll.Append_secondary("A", "A1")
ll.Append_secondary("A", "A2")
ll.Append_secondary("B", "B1")
ll.Append_secondary("B", "B2")
ll.Append_secondary("C", "C1")
ll.Append_secondary("C", "C2")
ll.Append_secondary("C", "C3")
ll.Append_secondary("B", "B3")
ll.Append_secondary("B", "B4")
ll.Delete_primary("A")
ll.Delete_secondary("B", "B3")
print(ll)

