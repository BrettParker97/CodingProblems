class Node:
  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def __repr__(self):
    return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

def recursion(node, base, res):
    #base case
    if node.right == None:
        temp = None
        if res != None:
            if node.value > base.value and node.value < res.value:
                return node
            else:
                return res
        else:
            return node
    
    #check this nodes value
    tempRes = None
    if node.value > base.value and node.value < res.value:
        tempRes = node
    else:
        tempRes = res
    
    #start recursion
    return recursion(node.right, base, tempRes)
    
def inorder_successor(node):
    parentSuc = None
    #check parent
    if node.parent != None:
        if node.parent.value > node.value:
            parentSuc = node.parent
    
    #check right child
    rightSuc = None
    if node.right != None:
        if parentSuc != None:
            rightSuc = recursion(node.right, node, parentSuc)
        else:
            rightSuc = recursion(node.right, node, None)
    
    #return based on results
    if parentSuc == None and rightSuc == None:
        return None
    elif parentSuc == None and rightSuc != None:
        return rightSuc
    elif parentSuc != None and rightSuc == None:
        return parentSuc
    else:
        if parentSuc.value > rightSuc.value:
            return rightSuc
        else:
            return parentSuc

tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left).value)
# 3
print(inorder_successor(tree.right).value)
# 5