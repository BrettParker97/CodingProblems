class Node:
    def __init__(self, value):
        self.value = value
        self.conns = []
        
    def deleteConn(self, value):
        for node in self.conns:
            if node.value == value:
                self.conns.remove(node)
       
def recursion(node, nodes):
    #end case
    if node.conns == []:
        del nodes[node.value]
        return
        
    connections = node.conns
    #delete x from its connections
    for x in connections:
        for y in x.conns:
            if y.value == node.value:
                x.conns.remove(node)
    
    #remove x from dict
    del nodes[node.value]
    
    #repeat on the previously disconnected nodes
    for x in connections:
        recursion(x, nodes)
    return
    
def num_connected_components(edges):
    nodes = {}
    #create graph, store in nodes dict
    for x in edges:
        #fetch or create graph nodes
        node1 = None
        if x[0] in nodes:
            node1 = nodes[x[0]]
        else:
            node1 = Node(x[0])
            nodes[x[0]] = node1
        node2 = None
        if x[1] in nodes:
            node2 = nodes[x[1]]
        else:
            node2 = Node(x[1])
            nodes[x[1]] = node2
        
        #connect them
        node1.conns.append(node2)
        node2.conns.append(node1)
    
    comps = 0
    #start deleteing nodes, when a node has 0 conns
    #we increase comps by 1
    while len(nodes) > 0:
        aNode = None
        for x in nodes:
            aNode = nodes[x]
            break    
        recursion(aNode, nodes)
        comps += 1
    return comps
            
print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2
