#The problem says to find inorder solution, however inorder
#doesnt keep the same root as inorder gives you the 
#order of the tree from left to right, therefor the root is the 
#left most leaf.
#The problem and example given hint toward finding preorder
#instead of inorder, so that is what im going to code instead.
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"({self.value}, {self.left}, {self.right})"

def recursion(node):
    #end case
    if node.left == None and node.right == None:
        return [node, node] #[head, tail]
    
    #check left
    leftRes = None 
    if node.left != None:
        leftRes = recursion(node.left)
    #check right
    rightRes = None
    if node.right != None:
        rightRes = recursion(node.right)
    
    #order the nodes
    #left != none, right DC
    if leftRes != None:
        node.right = leftRes[0]
        node.left = None
    #left == none, right DC
    else:
        node.right = rightRes[0]
        node.left = None
        return [node, rightRes[1]]
    
    #left != none, right != none
    if rightRes != None:
        leftRes[1].right = rightRes[0]
        return [node, rightRes[1]]
    #left != none, right == none
    else:
        return [node, leftRes[1]]
    

def flatten_bst(root):
    res = recursion(root)
    return None
    
  
n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

recursion(n1)
print(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
