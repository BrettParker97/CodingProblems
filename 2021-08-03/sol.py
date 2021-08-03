class Node:
  def __init__(self, value, adj=None):
    self.value = value
    self.adj = adj

    # Variable to help print graph
    self._print_visited = set()
    if self.adj is None:
      self.adj = []

  # Able to print graph
  def __repr__(self):
    if self in self._print_visited:
      return ''
    else:
      self._print_visited.add(self)
      final_str = ''
      for n in self.adj:
        final_str += f'{n}\n'

      self._print_visited.remove(self)
      return final_str + f'({self.value}, ({[n.value for n in self.adj]}))'

def recursion(node, visited):
    #end case(s)
    if node.adj == None:
        newNode = Node(node.value)
        visited.append(newNode)
        return newNode
    for x in visited:
        if x.value == node.value:
            return x
    
    #make a copy of me
    newMe = Node(node.value)
    newMe.adj = []
    visited.append(newMe)
    
    #check on the kids
    kids = []
    for x in node.adj:
        kids.append(recursion(x, visited))
    
    #add kids to adj list
    for x in kids:
        newMe.adj.append(x)
    return newMe
    
def deep_copy_graph(graph_node, visited=None):
    visited = []
    return recursion(graph_node, visited)
    
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]
graph_copy = deep_copy_graph(n1)
print(graph_copy)
# (2, ([4]))
# (4, ([3, 2]))
# (3, ([4]))
# (5, ([3]))
# (1, ([5]))