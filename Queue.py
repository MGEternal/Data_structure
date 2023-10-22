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
    def shuffle(self):
        Q_len = (len(self.items[0])//2)
        str = self.items[0]
        first = str[0:Q_len]
        second = str[Q_len:]
        Q1=Queue()
        Q2=Queue()
        list = []
        for i in first:
            Q1.enQueue(i)
        
        for j in second:
            Q2.enQueue(j)

        chk = 0
        for i in range(len(first)):
            list.append(Q1.deQueue())
            
            list.append(Q2.deQueue())
            
                
        return "".join(list)
Q = Queue()
Q.enQueue("ABCDEFGH")

res = Q.shuffle()
print(res)