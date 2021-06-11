class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def recursion(node, depth):
    #end case
    if node.left == None and node.right == None:
        return [node.value]
    
    #recurse
    depths = []
    if node.left != None:
        depths.append(recursion(node.left, depth + 1))
    if node.right != None:
        depths.append(recursion(node.right, depth + 1))
    
    #result
    #first split returned lists if theres multiple of
    #same sized path
    paths = []
    for x in depths:
        for y in x:
            if type(y) == list:
                paths.append(y)
            else:
                paths.append(x)
                break
    
    #find the longest path
    longest = 0
    for x in paths:
        if len(x) > 0:
            longest = len(x)
    
    #return all longest paths with the addition of
    #this node
    res = []
    for x in paths:
        if len(x) == longest:
            res.append([node.value] + x)
    return res

def largest_path_sum(tree):
    return recursion(tree, 0)
    
tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4

print(largest_path_sum(tree))
# [[1, 3, 5], [1, 2, 4]]