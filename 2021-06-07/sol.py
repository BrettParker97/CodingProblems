#finished in 23m 43s
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def addValue(node, level, res):
    if res.get(str(level)) == None:
        res[str(level)] = node.value
    else:
        res[str(level)] += node.value
    return res

def recursion(node, level, res):
    #base case
    if node.right == None and node.left == None:
        return addValue(node, level, res)
    
    #add current node
    res = addValue(node, level, res)
    
    #add right and left via recursion
    if node.right != None:
        res = recursion(node.right, level + 1, res)
    if node.left != None:
        res = recursion(node.left, level + 1, res)
    
    #return
    return res

def tree_level_max_sum(root):
    res = {}
    res = recursion(root, 0, res)
    keys = res.keys()
    best = 0
    result = None
    for x in keys:
        temp = res.get(x)
        if temp > best:
            result = x
            best = temp
    return result

n3 = Node(4, Node(3), Node(2))
n2 = Node(5, Node(4), Node(-1))
n1 = Node(1, n2, n3)

"""
    1          Level 0 - Sum: 1
   / \
  4   5        Level 1 - Sum: 9 
 / \ / \
3  2 4 -1      Level 2 - Sum: 8

"""

print(tree_level_max_sum(n1))
# Should print 1 as level 1 has the highest level sum