class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def getNodes(value, node):
    #end case
    if node.left == None and node.right == None:
        if node.value == value:
            return [node]
        else:
            return []
            
    #check this node
    res = []
    if node.value == value:
        res.append(node)
            
    #recursion on kids
    if node.left != None:
        temp = getNodes(value, node.left)
        if temp != []:
            res += temp
    if node.right != None:
        temp = getNodes(value, node.right)
        if temp != []:
            res += temp
    
    #return
    return res

def recursion(node, ref):
    #end case
    if ref.left == None and ref.right == None:
        if node.value == ref.value:
            return True
        else:
            return False
    
    #check this node
    if node.value != ref.value:
        return False
    
    #check vaild children
    temp = True
    if ref.left != None:
        if node.left == None:
            return False
        else:
            temp = recursion(node.left, ref.left)
        
        if temp == False:
            return False
    
    if ref.right != None:
        if node.right == None:
            return False
        else:
            temp = recursion(node.right, ref.right)
        
        if temp == False:
            return False
    
    #return
    return True
            
def find_subtree(s, t):
    matchingHeadNodes = getNodes(s.value, t)
    
    for x in matchingHeadNodes:
        temp = recursion(x, s)
        if temp == True:
            return True
    return False

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(find_subtree(s, t))
# True