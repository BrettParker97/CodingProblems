class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def recursion(node):
    #end case
    if node.left == None and node.right == None:
        return [[node.value]]
    
    #get values from children and add our value
    res = []
    if node.left != None:
        temp = recursion(node.left)
        for x in temp:
            res.append(x + [node.value])
    if node.right != None:
        temp = recursion(node.right)
        for x in temp:
            res.append(x + [node.value])
    return res

def target_sum_bst(root, target):
    #get all paths in tree
    res = recursion(root)
    
    #check all paths for sum(target)
    for x in res:
        temp = sum(x)
        if temp == target:
            #reverse the list to go from
            #root -> leaf instead of
            #leaf -> root
            temp2 = reversed(x)
            res2 = []
            for x in temp2:
                res2.append(x)
            return res2
            
    #if we dont find a match, then there is no path
    #that meets these reqs
    return False
  
#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(target_sum_bst(n1, 9))
# True
# Path from 1 -> 2 -> 6

print(target_sum_bst(n1, 7))
# False

print(target_sum_bst(n1, 8))
# True
# Path from 1 -> 3 -> 4