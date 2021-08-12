#In this problem, since there can be duplicates
#we cant just recurse down b and find the val so we must
#find the path from head to target

#Another problem with dups is that we cant just check
#the nodes kids (aka the whole branch) since there could be
#an exact dup of this branch somewhere else in the tree

#Therefore, my plan was to match the class value of our target
#node to the node in a, as I do that I take note of the path
#then use that path to decend the 2nd tree
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def getPath(node, target):
    #end case(s)
    if node == target:
        return [target.val]
    if node.left == None and node.right == None:
        return None
    
    #check on the kids
    leftRes = None
    if node.left != None:
        leftRes = getPath(node.left, target)
    rightRes = None
    if node.right != None:
        rightRes = getPath(node.right, target)
    
    #check if we found a path
    if leftRes != None:
        return leftRes + [node.val]
    if rightRes != None:
        return rightRes + [node.val]
    return None
    
def findNode(a, b, node):
    pathRes = getPath(a, node)
    path = list(reversed(pathRes))
    
    #use path to find node in b
    res = None
    currentNode = b
    for x in range(len(path)):
        #start
        if currentNode.val == path[x]:
            continue
        
        #check on the kids
        if currentNode.left != None:
            if currentNode.left.val == path[x]:
                currentNode = currentNode.left
                continue
        if currentNode.right != None:
            if currentNode.right.val == path[x]:
                currentNode = currentNode.right
                continue
    return currentNode.val
    
#  1
# / \
#2   3
#   / \
#  4*  5
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.right.left = Node(4)
a.right.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.right.left = Node(4)
b.right.right = Node(5)

print(findNode(a, b, a.right.left))
# 4