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
        return [[node.value]]
    
    #check kids
    leftRes = None
    if node.left != None:
        leftRes = recursion(node.left)
        
    rightRes = None
    if node.right != None:
        rightRes = recursion(node.right)
    
    #return all combinations
    res = []
    for x in leftRes:
        res.append([node.value] + x)
    for x in rightRes:
        res.append([node.value] + x)
    return res
    
def bst_numbers_sum(root, num=0):
    #get all paths
    res = recursion(root)
    
    #convert them to ints and add together
    res2 = 0
    for x in res:
        val = ""
        for y in x:
            val += f"{y}"
        val = int(val)
        res2 += val
        print(val)
    return res2

n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262