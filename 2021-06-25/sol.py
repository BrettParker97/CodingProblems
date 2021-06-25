class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    
  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"

def splitTree(parent, node, s, greater):
    #end case
    if greater:
        if node.value > s:
            if parent.left == node:
                parent.left = None
            else:
                parent.right == None
            return (node, parent)
        elif node.right == None:
            return None
    elif not greater:    
        if node.value <= s:
            if parent.left == node:
                parent.left = None
            else:
                parent.right == None
            return (node, parent)
    else:
        return None
    
    #recursion
    if greater:
        return splitTree(node, node.right, s, greater)
    else:
        return splitTree(node, node.left, s, greater)
    
def split_bst(bst, s):
    res = splitTree(None, bst, s, False)
    leftRoot = res[0]
    rightRoot = bst
    breakPoint = res[1]
    
    res2 = splitTree(None, leftRoot, s, True)
    if breakPoint != None:
        breakPoint.left = res2
    else:
        breakPoint = res2
    return (res)
  
n2 = Node(2)
n1 = Node(1, None, n2)

n5 = Node(5)
n4 = Node(4, None, n5)

root = Node(3, n1, n4)

print(root)
# (3, (1, (2)), (4, None, (5)))
# How the tree looks like
#     3
#   /   \
#  1     4
#   \     \
#    2     5

print(split_bst(root, 2))
# ((1, None, (2)), (3, None, (4, None, (5))))
# Split into two trees
# 1    And   3
#  \          \
#   2          4
#               \
#                5