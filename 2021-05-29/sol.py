

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"
    
def swap(aList):
    futureHead = None
    try:            
        futureHead = aList.next
    except:
        return aList
        
    head = aList
    node1 = None
    node2 = None
    
    x = 0
    while True:
        if x == 0:
            node1 = aList
        elif x % 2 == 0:
            if head.next != None:
                node1 = head.next
            else:
                break
        elif x % 2 == 1:
            if node1.next != None:
                node2 = node1.next
            else:
                break
            
            node3 = None
            if node2.next != None:
                node3 = node2.next
            
            head.next = node2
            node2.next = node1
            
            if node3 != None:
                node1.next = node3
                head = node1
            else:
                break
                
        x += 1
    return futureHead
            
aList = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap(aList))