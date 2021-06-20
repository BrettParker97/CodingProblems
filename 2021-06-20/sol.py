class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"
    
def remove_dup(lst):
    #store values we have seen
    occur = []
    
    #init values
    head = lst
    occur.append(head.value)
    node = None
    if head.next != None:
        node = head.next
    else:
        return head
        
    #loop through all nodes in list
    while True:
        #end case
        if node.next == None:
            if node.value in occur:
                head.next = None
            return
        
        #check
        if node.value in occur:
            head.next = node.next
            node = node.next
        else:
            occur.append(node.value)
            head = node
            node = node.next

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))