def recursion(position, height, width, mat):
    positionPrice = mat[position[0]][position[1]]
    
    #end case
    if position[0] + 1 >= width and position[1] + 1 >= height:
        return mat[position[0]][position[1]]
    
    #recursion
    rightPrice = None
    downPrice = None
    if position[0] + 1 < width:
        rightPos = (position[0] + 1, position[1])
        rightPrice = recursion(rightPos, height, width, mat)
    if position[1] + 1 < height:
        downPos = (position[0], position[1] + 1)
        downPrice = recursion(downPos, height, width, mat)
    
    #return
    returnPrice = positionPrice
    if rightPrice != None:
        returnPrice += rightPrice
    
    if downPrice != None and positionPrice + downPrice > returnPrice:
        returnPrice = positionPrice + downPrice
        
    return returnPrice
    

def max_change(mat):
    return recursion((0, 0), len(mat[0]), len(mat), mat)

mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13